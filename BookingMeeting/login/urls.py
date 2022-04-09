from django.contrib import admin
from django.urls import path


from .views import RegisterView  # Import the view here



from django.conf import settings
from django.conf.urls.static import static
  
# importing views from views..py

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
    
    path('user_profile/<str:pk>', views.user_profile, name='user_profile'),
    path('test', views.test, name='test'),
    path('register/', RegisterView.as_view(), name='users-register'),  # This is what we added
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


