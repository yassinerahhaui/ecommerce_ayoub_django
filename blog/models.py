from django.db import models

# Create your models here.

class Article(models.Model):
    title_fr = models.CharField(max_length=250)
    title_ar = models.CharField(max_length=250)
    paragraph_fr_1 = models.TextField(max_length=1000,null=True)
    paragraph_ar_1 = models.TextField(max_length=1000,null=True)
    paragraph_fr_2 = models.TextField(max_length=1000,null=True,blank=True)
    paragraph_ar_2 = models.TextField(max_length=1000,null=True,blank=True)
    paragraph_fr_3 = models.TextField(max_length=1000,null=True,blank=True)
    paragraph_ar_3 = models.TextField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='blog',null=True)
    image_2 = models.ImageField(upload_to='blog',null=True,blank=True)
    image_3 = models.ImageField(upload_to='blog',null=True,blank=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    last_update = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title_fr