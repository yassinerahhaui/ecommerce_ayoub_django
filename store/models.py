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
  description_fr = models.TextField(max_length=1000,null=True)
  price = models.DecimalField(max_digits=10,decimal_places=2)
  old_price = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
  sale = models.BooleanField(default=False)
  in_stock = models.BooleanField(default=True)
  quantity = models.IntegerField(default=1)
  delivery = models.CharField(max_length=150)
  created_at = models.DateTimeField(auto_now=True)
  image = models.ImageField(upload_to=product_upload,max_length=500)
  image1 = models.ImageField(upload_to=product_upload,max_length=500)
  image2 = models.ImageField(upload_to=product_upload,max_length=500)
  image3 = models.ImageField(upload_to=product_upload,max_length=500)
  image4 = models.ImageField(upload_to=product_upload,max_length=500)
  image5 = models.ImageField(upload_to=product_upload,max_length=500)
  collection = models.ForeignKey(Collection, related_name="product_collection",on_delete=models.DO_NOTHING,null=True,blank=True)
  category = models.ForeignKey(Category, related_name="product_category", on_delete=models.CASCADE,null=True)

  def save(self, *args, **kwargs):
    if self.quantity < 1:
      self.in_stock = False
    else:
      self.in_stock = True
    super().save(*args, **kwargs)

  def __str__(self):
    return self.name_fr

