from django.urls import path
  
# importing views from views..py

from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('base', views.home),
    path('help', views.help),
    path('room/<str:pk>', views.room, name="room"),
    path('room', views.room),
    path('welcome', views.welcome, name="welcome"),
    path('', views.welcome, name='welcome'),
    
    
]