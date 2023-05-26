from django.db import models
from accountdata.models import appuser
from django.utils import timezone


class Post(models.Model):

    NUMBER_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    id = models.AutoField(primary_key=True, null=False, blank=False) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(appuser, null=True, blank=True, on_delete=models.CASCADE)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    personnel = models.IntegerField(choices=NUMBER_CHOICES, default=1)
    created_at = models.DateTimeField('created_time', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('updated_time', auto_now=True, null=True)



    def __str__(self):
        return self.title