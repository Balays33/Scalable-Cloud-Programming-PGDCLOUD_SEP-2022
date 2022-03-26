from django.shortcuts import render, redirect
from django.contrib import messages                             # django flash messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout   #user autheticate
from django.contrib.auth.decorators import login_required     # user  wants to acces a page
from .forms import CustomUserCreationForm                     # user registration form
#from django.contrib.auth.forms import CustomUserCreationForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .models import      # import model
from django.http import Http404
#import requests

"""
def index(request):
    return HttpResponse("Hello, world. You're at the login index.")
    
"""


# Create your views here.
#index page view
def index(request):
    print("index page")
    return render(request, "login/index.html" )
    
    


# Create your views here.
#login/registration page view
def loginUser(request):
    print('login page')
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            print('ERROR')
            
        user = authenticate(request, username=username, password=password)
        print('USER:',user)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR password does not exit')
    
    return render(request, 'login/login_register.html', {'page': page})
    
    
def logoutUser(request):
    print("logoutUser page")
    logout(request)
    return redirect('loginUser')

def registerUser(request):
    print('user registration')
    page = 'register'
    print('page:',page)

    """
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
"""
    
    """
    
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            if user is not None:
                login(request, user)
                return redirect('gallery')
                context = {'form': form, 'page': page}
    """
    
    return render(request, 'login/login_register.html', {'page': page})
    
     
    
# Create your views here.
#registration page view
def user_profile(request):
    print("user_profile page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print('USER:',user)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, "login/user_profile.html" )
    


#test page view
@login_required(login_url='login')
def test(request):
    print("test page")
    
    return render(request, "login/test.html" )
   
    