from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSer

class BestChoices(APIView):
    def get(self, request, format=None):
        obj = Product.objects.all()[:10].order_by('-id')
        serializer = ProductSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

