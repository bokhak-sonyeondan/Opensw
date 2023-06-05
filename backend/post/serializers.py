from rest_framework import serializers
from .models import Post
from chat.models import ChatRoom

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # post 작성 및 수정시 들어갈 정보, user를 serializer에 포함하면 게시글에서 유저를 고르는 일이 발생하기 때문에 제외
        # 유효성 검사는 views.py에서 구현
        fields = ( 
            'id',
            'title',
            'content',
            'lat',
            'lng',
            'personnel',
            'created_at',
            'updated_at',
            'reciveuser',
            'match',
            'roomnum',
            'user',
            'gender',
            'major',
            'phone',
            'age',
        )
        model = Post
        
        
    def update(self, instance, validated_data):
        request = self.context['request']
        if instance.user != request.user:
            instance.reciveuser = request.user
            instance.match=1
            chat_room = ChatRoom.objects.create()
            chat_room.participants.set([instance.user, instance.reciveuser]) # user1과 user2를 채팅방에 추가
            chat_room.save()
            instance.roomnum = chat_room.id 

            instance.save()
        
            return instance
