
from django.urls import path, include
from rest_framework import routers
from QuanLyApp import views


routers = routers.DefaultRouter()
routers.register('category', views.CategoryViewSet, basename='category' )


urlpatterns = [
    path('', include(routers.urls))
]
