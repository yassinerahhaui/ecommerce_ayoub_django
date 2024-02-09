from django.urls import path
from .views import BestChoices, ProductList, ProductDetails

app_name='store'

urlpatterns= [
  path('best-choices',BestChoices.as_view(),name='best-choices'),
  path('product/list',ProductList.as_view(),name='product-list'),
  path('product/<int:pk>',ProductDetails.as_view(),name='product-details'),
]