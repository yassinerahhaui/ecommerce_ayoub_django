from django.db import models

# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,null=True)

    def __str__(self):
        return self.email
    

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,null=True)
    subject = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.email