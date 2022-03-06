from django.contrib import admin
from django.urls import path
  
# importing views from views..py

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.index),
    
]


