from django.urls import path
from .views import BestChoices
app_name='store'

urlpatterns= [
  path('best-choices',BestChoices.as_view(),name='best-choices'),
]