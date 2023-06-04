# Create your views here.
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework import status

from rest_framework.decorators import api_view
from django.db.models import Q

class ListPost(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
     
    def get(self, request):
        current_user = request.user
        if request.user.is_authenticated:
            posts = Post.objects.filter(Q(match=0) | (Q(match=1) & (Q(postuser=current_user) | Q(reciveuser=current_user))))
            serializer = PostSerializer(posts, many=True, context={'request': request})
            return Response(serializer.data)    
        else: 
            return Response({'detail': '로그인 하십시오.'}, status=status.HTTP_401_UNAUTHORIZED)
     
    def create(self, request, *args, **kwargs):
        # 요청 데이터에서 필요한 필드만 추출하여 새로운 데이터 생성
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'person': request.data.get('person'),
            'postuser': request.user.id,  # 현재 로그인된 사용자의 phone 사용
            'postphone':request.user.phone,
            'lat':request.data.get('lat'),
            'lng':request.data.get('lng'),
        }

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from chat.models import ChatRoom
from django.shortcuts import redirect

class DetailPost(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.match ==1:
            if  (instance.postuser == request.user) | (instance.reciveuser == request.user):
                serializer = self.get_serializer(instance)
                url = "http://127.0.0.1:8000/chat/room/" + str(instance.roomnum) + "/"
                print(url)
                return redirect(url)
                #return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'You are not authorized to view this post'},
                                status=status.HTTP_403_FORBIDDEN)
                
        else:
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        if instance.match == 1:
        
            return Response({'detail': 'matched'},
                                status=status.HTTP_403_FORBIDDEN)
        
        elif Q(instance.match == 0) & Q(instance.postuser == request.user):
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
            
            if 'recivertext' in request.data:
                instance.recivertext = request.data.get('recivertext')
                instance.reciveuser = request.user
                instance.reciverphone = request.user.phone
                
                instance.match=1
                chat_room = ChatRoom.objects.create()
                chat_room.participants.set([instance.postuser, instance.reciveuser]) # user1과 user2를 채팅방에 추가
                chat_room.save()
                instance.roomnum = chat_room.id 
    
    
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}

            return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_post_list(request):
    current_user = request.user
    if request.user.is_authenticated:
        posts = Post.objects.filter(Q(match=0) | (Q(match=1) & (Q(postuser=current_user) | Q(reciveuser=current_user))))
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)    
    else: 
        return Response({'detail': '로그인 하십시오.'}, status=status.HTTP_401_UNAUTHORIZED)