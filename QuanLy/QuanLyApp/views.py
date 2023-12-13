from rest_framework import viewsets, generics
from .models import Category
from QuanLyApp import serializers


# Create your views here.
class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
