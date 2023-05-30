# Create your models here.
from django.db import models

#Post model
class Post(models.Model):                               #┏━━━━━━┓#
    title   = models.CharField(max_length=200)          #┃ title 컬럼 ┃#
    content = models.TextField()                        #┃content 컬럼┃#
    person  = models.IntegerField(default=1,null=True)  #┃몇대몇 미팅?┃#
    lat     = models.FloatField(default=0,null=True)    #┃    위도    ┃#
    lng     = models.FloatField(default=0,null=True)    #┃    경도    ┃#
                                                        #┗━━━━━━┛#

    def __str__(self):
        """A string representation of the model."""
        return self.title