from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField(null=False)
    writer = models.CharField(max_length=10, null=False, default='')
    
    date =  models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)    
    
    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname