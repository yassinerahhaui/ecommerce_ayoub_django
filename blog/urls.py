from django.urls import path
from .views import BestArticles, ArticleList, ArticleDetails

app_name="blog"

urlpatterns = [
    path('best-articles',BestArticles.as_view(),name='best-articles'),
    path('article/list',ArticleList.as_view(),name='article-list'),
    path('article/<int:pk>',ArticleDetails.as_view(),name='article-details'),
]
