from django.urls import path
  
# importing views from views..py

from . import views

urlpatterns = [
    path('', views.calendarview, name='calendarview'),
    path('calendar', views.calendarview),
    
]