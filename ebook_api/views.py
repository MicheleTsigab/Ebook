from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import *
from .serializers import authored_ebookserializer, authorserializer, bought_ebookserializer, customerserializer, ebookserializer
#@api_view()
#def first_api_view(request):
 #   ebooks=ebook.objects.all()
  #  ebook_serializers=ebookserializer(ebooks,many=True)
   # return Response(ebook_serializers.data)
class authorViewset(viewsets.ModelViewSet):
    serializer_class = authorserializer
    queryset = author.objects.all()
class customerViewset(viewsets.ModelViewSet):
    serializer_class = customerserializer
    queryset=customer.objects.all()
class ebookViewset(viewsets.ModelViewSet):
    serializer_class = ebookserializer
    queryset=ebook.objects.all()
class reviewViewset(viewsets.ModelViewSet):
    serializer_class = customerserializer
    queryset=customer.objects.all()
class authored_ebook(viewsets.ModelViewSet):
    serializer_class = authored_ebookserializer
    queryset=authored_ebook.objects.all()
class bought_ebook(viewsets.ModelViewSet):
    serializer_class = bought_ebookserializer
    queryset=bought_ebook.objects.all()
