from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post

User = get_user_model()
from chat.models import ChatRoom

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content','match', 'person', 'postuser','reciveuser','recivertext',
                  'reciverphone','postphone','lat','lan')

        

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['postuser'] = user
        validated_data['postphone'] = user.phone
        post = Post.objects.create(**validated_data)
        return post
    
    def update(self, instance, validated_data):
        request = self.context['request']
        if instance.postuser != request.user:
            instance.reciveuser = request.user
            instance.reciverphone = request.user.phone
            instance.match=1
            chat_room = ChatRoom.objects.create()
            chat_room.participants.set([instance.postuser, instance.reciveuser]) # user1과 user2를 채팅방에 추가
            chat_room.save()
        
        if 'recivertext' in validated_data:
            instance.recivertext = validated_data['recivertext']
        instance.save()
        
        return instance
