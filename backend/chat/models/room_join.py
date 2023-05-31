from django.db import models

from chat.models.base_model import BaseModel
from chat.models.room import Room
from accountdata.models import appuser


class RoomJoin(BaseModel):

    user_id = models.ForeignKey(appuser, on_delete=models.CASCADE, related_name="roomJoin", db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="roomJoin", db_column="room_id")

    class Meta:
        db_table = "roomJoin"