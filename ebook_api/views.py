from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets

from .models import *
from .serializers import authorserializer, ebookserializer
@api_view()
def first_api_view(request):
    ebooks=ebook.objects.all()
    ebook_serializers=ebookserializer(ebooks,many=True)
    return Response(ebook_serializers.data)
class authorViewset(viewsets.ModelViewSet):
    serializer_class = authorserializer
    queryset = author.objects.all()
