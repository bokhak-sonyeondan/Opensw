from django.db import models
from django.contrib.auth import get_user_model
from accountdata.models import appuser

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=200) # title 컬럼
    content = models.TextField()           # content 컬럼
    person = models.IntegerField(null=True)  
    match = models.IntegerField(default=0,null=True)
    postuser=models.ForeignKey(User, on_delete=models.CASCADE, null=True,related_name='posts_sent',blank=True)
    reciveuser=models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='posts_received',blank=True)
    reciverphone = models.CharField(max_length=30, null=True,blank=True)
    postphone = models.CharField(max_length=30,null=True,blank=True)
    recivertext = models.TextField(null=True,blank=True)
    lat = models.FloatField(default=0,null=True,blank=True)#위도
    lan = models.FloatField(default=0,null=True,blank=True)#경도
    def __str__(self):
        return self.title