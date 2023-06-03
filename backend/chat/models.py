from django.db import models
from accountdata.models import appuser

class ChatRoom(models.Model):
    id = models.AutoField(primary_key=True)
    participants = models.ManyToManyField(appuser)
    created_at = models.DateTimeField(auto_now_add=True)

    # 추가적인 필드들을 정의할 수 있습니다.

    def __str__(self):
        return f"Chat Room ({self.pk})"
    
class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.TextField(null=True,blank=True)
    
    
"""chat_room = ChatRoom.objects.create()
chat_room.participants.add(user1, user2)  # user1과 user2를 채팅방에 추가
        """