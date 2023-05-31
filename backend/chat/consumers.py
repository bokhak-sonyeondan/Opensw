# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatMessage, ChatRoom


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        self.room_group_name = f"chat_{self.room_id}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
    
    async def get_chat_room(self, room_id):
    # Perform the necessary database query to retrieve the chat room
    # For example, you can use the ChatRoom.objects.get() method
        try:
            chat_room = ChatRoom.objects.get(id=room_id)
        except ChatRoom.DoesNotExist:
        # Handle the case when the chat room does not exist
        # For example, raise an exception or return None
            raise Exception("Chat room does not exist")

        return chat_room
        
        
"""
from asgiref.sync import sync_to_async
        
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        if self.room_id:
            self.room_group_name = f"chat_{self.room_id}"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
        # Handle case when room_id is empty
            raise ValueError("No room_id provided")
        # Join room group
        #await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        #await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

    # Save message to the database
        await self.save_message(message)

    # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
    )

# Save message to the database
    async def save_message(self, message):
        room = await self.get_chat_room(self.room_id)

    # Create a new ChatMessage object and associate it with the room
        await sync_to_async(ChatMessage.objects.create)(room=room, message=message)

    # Additional logic for saving the message

    # Additional logic for saving the message

# Retrieve the chat room from the database
    async def get_chat_room(self, room_id):
    # Perform the necessary database query to retrieve the chat room
    # For example, you can use the ChatRoom.objects.get() method
        try:
            chat_room = ChatRoom.objects.get(id=room_id)
        except ChatRoom.DoesNotExist:
        # Handle the case when the chat room does not exist
        # For example, raise an exception or return None
            raise Exception("Chat room does not exist")

        return chat_room"""
