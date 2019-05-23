from django.urls import path, include
from django.contrib import admin
from .views import post_list

urlpatterns = [
    path('', post_list, name='post_list')
]