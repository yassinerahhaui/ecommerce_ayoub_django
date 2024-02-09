from django.db import models
import uuid
# Create your models here.
def collection_upload(instance,filename):
  ext = filename.split('.')[-1]
  return f'collection/{uuid.uuid4}.{ext}'

class Collection(models.Model):
  name_fr = models.CharField(max_length=150)
  name_ar = models.CharField(max_length=150)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  image = models.ImageField(upload_to=collection_upload,max_length=500,null=True)

  def __str__(self):
    return self.name_fr

class Category(models.Model):
  name_fr = models.CharField(max_length=150)
  name_ar = models.CharField(max_length=150)

  def __str__(self):
    return self.name_fr

def product_upload(instance,filename):
  ext = filename.split('.')[-1]
  return f'products/{instance.name_fr}/{uuid.uuid4}.{ext}'

class Product(models.Model):
  name_fr = models.CharField(max_length=150)
  name_ar = models.CharField(max_length=150)
  description_fr = models.TextField(max_length=1000,null=True)
  description_ar = models.TextField(max_length=1000,null=True)
  details_fr = models.TextField(max_length=10000,null=True,blank=True)
  details_ar = models.TextField(max_length=10000,null=True,blank=True)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  old_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
  created_at = models.DateTimeField(auto_now=True)
  last_update = models.DateTimeField(auto_now_add=True,null=True)
  image = models.ImageField(upload_to=product_upload,max_length=500)
  quantity = models.IntegerField(default=1)
  category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE,null=True)

  def __str__(self):
    return self.name_fr

