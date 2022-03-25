from django.contrib import admin
from django.urls import path
  
# importing views from views..py

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    
    path('user_profile', views.user_profile, name='user_profile'),
    path('test', views.test, name='test'),
    
]


