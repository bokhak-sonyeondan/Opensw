from django.urls import path

from . import views
from .views import ChatRoomListAPIView

urlpatterns = [
    path("", views.index, name="index"),
    path("room/<int:room_id>/", views.room),
    path('see/rooms/', ChatRoomListAPIView.as_view(), name='chat-room-list'),
]