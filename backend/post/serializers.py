from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
            'lat',
            'lng',
            'personnel',
            'created_at',
            'updated_at'
        )
        model = Post