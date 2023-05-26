
from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

class ListPost(generics.ListCreateAPIView): #작성
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailPost(generics.RetrieveUpdateDestroyAPIView): #세부정보, 수정, 삭제
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self): #로그인 대상이 맞는지 확인
        obj = super().get_object()
        if obj.user != self.request.user:
            raise permissions.PermissionDenied
        return obj