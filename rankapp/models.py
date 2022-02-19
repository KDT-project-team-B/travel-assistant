from django.db import models

# Create your models here.
#맛집 DB
class Data(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class jejusi_food(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class haeundae_food(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class seomyun_food(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class gyodong_food(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class chodangdong_food(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
 #숙소 DB   
class seoguipo_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class jejusi_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class haeundae_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class seomyun_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class gyodong_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class chodangdong_rest(models.Model):
    title = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    