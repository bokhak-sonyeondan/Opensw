from django.shortcuts import render


def index(request):
    return render(request, "chat/index.html")


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

@login_required
def room(request, room_id):
    try:
        chat_room = ChatRoom.objects.get(id=room_id)
        
        # 채팅방에 속해 있는지 확인하는 로직을 구현
        if request.user in chat_room.participants.all():
            print('승인')
            return render(request, "chat/room.html", {"room_id": room_id, 'realname': request.user.realname})
        else:
            print('거절')
            return render(request, "chat/access_denied.html")
    except ChatRoom.DoesNotExist:
        # 채팅방이 없을 경우 예외 처리
        return render(request, "chat/chatroom_not_found.html")




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatRoom
from .serializers import ChatRoomSerializer

"""class ChatRoomListAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.user.id
        chat_rooms = ChatRoom.objects.filter(participants__id=user_id)
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    """
    
class ChatRoomListAPIView(APIView):
    def get(self, request, format=None):
        chat_rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer(chat_rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)