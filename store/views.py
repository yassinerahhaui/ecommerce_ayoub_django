from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSer

class BestChoices(APIView):
    def get(self, request, format=None):
        obj = Product.objects.all().order_by('-id')[:10]
        serializer = ProductSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ProductList(APIView):
    def get(self,request,format=None):
        obj = Product.objects.all().order_by('-id')
        serializer = ProductSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ProductDetails(APIView):
    def get_object(self,pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ProductSer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


