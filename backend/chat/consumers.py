# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.shortcuts import render, redirect
from .models import ChatMessage, ChatRoom
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async



class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        # 채팅방에 입장할 때 저장된 채팅 메시지 가져오기
        messages = await self.get_chat_messages()

        # 클라이언트에 채팅 메시지 전송
        await self.send_chat_messages(messages)
        
    @database_sync_to_async
    def get_chat_messages(self):
        room = ChatRoom.objects.get(pk=self.room_id)
        messages = room.chatmessage_set.order_by('id')
        return [message.message for message in messages]

    async def send_chat_messages(self, messages):
        for message in messages:
            await self.send(text_data=json.dumps({
                'type': 'chat.message',
                'message': message
            }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def save_message(self, message):
        room = ChatRoom.objects.get(pk=self.room_id)
        ChatMessage.objects.create(room=room, message=message)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json.get('type') == 'chat.delete_room':
            await self.delete_chat_room()
            
        else:
            username = text_data_json['username']  # 사용자 이름
            message = text_data_json['message']  # 채팅 메시지
    # 채팅 메시지 앞에 사용자 이름을 추가하여 전송하는 로직
            final_message = f"{username}: {message}"
        
    # 채팅 메시지를 저장하고 전송하는 로직 구현

            await self.save_message(final_message)

    # 다른 클라이언트에게 전송
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat.message",
                    "message": final_message
                }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
    
    
    async def get_chat_room(self, room_id):
        try:
            chat_room = ChatRoom.objects.get(id=room_id)
        except ChatRoom.DoesNotExist:
            raise Exception("Chat room does not exist")

        return chat_room
    
    
    from asgiref.sync import async_to_sync

    @sync_to_async
    def delete_chat_room(self):
        # 채팅방 삭제 로직
        room = ChatRoom.objects.get(pk=self.room_id)
        room.delete()
        
    