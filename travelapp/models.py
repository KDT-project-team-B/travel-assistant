from django.db import models

# Create your models here.
#서귀포 맛집
class sample(models.Model):
    name = models.CharField(max_length=255)
    sc = models.CharField(max_length=255)
    a = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

#제주시 맛집
class jeju(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

#해운대
class haeundae(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
#서면
class seomyun(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
#교동
class gyodong(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
#초당
class chodang(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
#숙소   
class seoguiporest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class jejurest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class haeundaerest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class seomyunrest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class gyodongrest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
class chodangrest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title