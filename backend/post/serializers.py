from rest_framework import serializers
from .models import Post

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
            'user',
            'gender',
            'major',
            'phone',
            'age',
            'realname',
            'recievuser',
        )
        model = Post
        