from django.db import models

from chat.models.base_model import BaseModel
from chat.models.room import Room
from accountdata.models import appuser


class Message(BaseModel):
    message = models.CharField(max_length=500)
    user_id = models.ForeignKey(appuser, on_delete=models.CASCADE, related_name="message", db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="message", db_column="room_id")

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.user_id.email

    def last_30_messages(self, room_id):
        return Message.objects.filter(room_id=room_id).order_by('created_at')[:30]