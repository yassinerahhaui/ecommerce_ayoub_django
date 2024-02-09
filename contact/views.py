from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Newsletter, ContactUs
from .serializers import NewsletterSer, ContactUsSer

class NewsletterView(APIView):
    def get(self, request, format=None):
        obj = Newsletter.objects.all()
        serializer = NewsletterSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = NewsletterSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ContactUsView(APIView):
    def get(self, request, format=None):
        obj = ContactUs.objects.all()
        serializer = ContactUsSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = ContactUsSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)




