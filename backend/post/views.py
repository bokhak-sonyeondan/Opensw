from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView): # 작성
    queryset = Post.objects.all() # 객체 설정
    serializer_class = PostSerializer # 직렬화 (json으로 변경)
    permission_classes = [permissions.IsAuthenticated] # 인증된 사용자인지 확인

    def perform_create(self, serializer): # user 필드를 현재 사용자로 설정
        user = self.request.user
        serializer.save(user = user,
                        phone=user.phone,
                        age=user.age,
                        gender=user.gender,
                        major=user.major,
                        )
        


from rest_framework.response import Response
from chat.models import ChatRoom
from rest_framework import status
from django.db.models import Q

class DetailPost(generics.RetrieveUpdateDestroyAPIView): # 세부정보, 수정, 삭제
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
    def get_object(self): # 로그인 대상이 맞는지 확인(user 필드 비교)
        obj = super().get_object()
        if obj.user != self.request.user:
            raise permissions.PermissionDenied
        return obj"""
    
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        if instance.match == 1:
        
            return Response({'detail': 'matched'},
                                status=status.HTTP_403_FORBIDDEN)
        
        elif Q(instance.match == 0) & Q(instance.user == request.user):
            instance.content = request.data.get('content')
            instance.title = request.data.get('title')
            instance.person = request.data.get('person')
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        elif Q(instance.match == 0) & Q(instance.postuser != request.user):
            
            instance.reciveuser = request.user
                
            instance.match=1
            chat_room = ChatRoom.objects.create()
            chat_room.participants.set([instance.user, instance.reciveuser]) # user1과 user2를 채팅방에 추가
            chat_room.save()
            instance.roomnum = chat_room.id 
    
    
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data, status=status.HTTP_200_OK)