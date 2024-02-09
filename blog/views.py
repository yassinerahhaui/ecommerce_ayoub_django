from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSer

class BestArticles(APIView):
    def get(self, request, format=None):
        obj = Article.objects.all().order_by('-id')[:4]
        serializer = ArticleSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ArticleList(APIView):
    def get(self, request, format=None):
        obj = Article.objects.all().order_by('-id')
        serializer = ArticleSer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ArticleDetails(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ArticleSer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
