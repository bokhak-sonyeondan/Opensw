from django.db import models
from accountdata.models import appuser
from django.utils import timezone

class Post(models.Model):

    NUMBER_CHOICES = [ # 인원수 1~5까지
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    id = models.AutoField(primary_key=True, null=False, blank=False) # post한 게시글 고유번호
    title = models.CharField(max_length=100) # 제목
    content = models.TextField() # 내용
    user = models.ForeignKey(appuser, null=True, blank=True, on_delete=models.CASCADE) # post한 유저의 model
    lat = models.FloatField(default=0) # 위도
    lng = models.FloatField(default=0) # 경도
    personnel = models.IntegerField(choices=NUMBER_CHOICES, default=1) # 인원수
    created_at = models.DateTimeField('created_time', auto_now_add=True, null=True) # 작성 시간
    updated_at = models.DateTimeField('updated_time', auto_now=True, null=True) # 수정 시간
    gender = models.CharField(max_length=1,null=True,blank=True)
    major = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=30,null=True,blank=True)
    age = models.IntegerField(default=20,null=True,blank=True)
    realname = models.CharField(max_length=100,null=True,blank=True)
    reciveuser=models.ForeignKey(appuser, on_delete=models.CASCADE, null=True, related_name='posts_received',blank=True)
        
    
    
    def __str__(self):
        return self.title