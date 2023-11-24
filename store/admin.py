from django.contrib import admin
from .models import Product, Collection, Category
# Register your models here.

admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Category)
