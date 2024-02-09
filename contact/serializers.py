from rest_framework import serializers
from .models import Newsletter, ContactUs

class NewsletterSer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = '__all__'

class ContactUsSer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'
