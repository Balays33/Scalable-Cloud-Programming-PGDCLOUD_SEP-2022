from django.contrib import admin
from django.urls import path


from .views import  profile, RegisterView


from django.conf import settings
from django.conf.urls.static import static
  
# importing views from views..py

from . import views

##################### serializer

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

########################

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='loginUser'),
    path('logout', views.logoutUser, name="logout"),
    path('register', views.registerUser, name="register"),
    
    path('user_profile/<str:pk>', views.user_profile, name='user_profile'),
    path('test', views.test, name='test'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    
    
    #############################
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ##############################
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


