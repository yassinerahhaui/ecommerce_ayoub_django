from django.urls import path
from .views import ContactUsView, NewsletterView
app_name="contact"

urlpatterns = [
    path('contact/create',ContactUsView.as_view(),name='contact-us'),
    path('newsletter/create',NewsletterView.as_view(),name='newsletter'),
]
