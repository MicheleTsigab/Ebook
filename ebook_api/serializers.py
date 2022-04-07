from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined']
        #fields='__all__'
class ebookserializer(serializers.ModelSerializer):
    class Meta:
        model=ebook
        fields='__all__'
class customerserializer(serializers.ModelSerializer):
    customer=userserializer()
    class Meta:
        model=customer
        fields=['customer','bought_ebooks']
        
class authorserializer(serializers.ModelSerializer):
    author=userserializer()
    class Meta:
        model=author
        fields=['id','author']
        #fields='__all__'
class authored_ebookserializer(serializers.ModelSerializer):
    ebook=ebookserializer()
    author=authorserializer()
    class Meta:
        model=authored_ebook
        fields=['ebook','author','date']
class bought_ebookserializer(serializers.ModelSerializer):
    class Meta:
        model=bought_ebook
        fields=['__all__']
class genreserializer(serializers.ModelSerializer):
    class Meta:
        model=genre
        fields=['__all__']
class reviewserializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['__all__']
class discount(serializers.ModelSerializer):
    class Meta:
        model=discount
        fields=['__all__']