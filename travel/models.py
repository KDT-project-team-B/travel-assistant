from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('travel/review.html', args=[self.name])
    
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField(null=False)
    writer = models.CharField(max_length=10, null=False, default='')
    
    date =  models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)  
    
    hits = models.PositiveIntegerField(default=0)  
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    
    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname
    
    @property
    def counter(self):
        self.hits = self.hits + 1
        self.save()
    
class Answer(models.Model):
    postname = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)  

