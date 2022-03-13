from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout   #user autheticate
from django.contrib.auth.decorators import login_required


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
    print('login/registration page')
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        print('USER:',user)
        print('test')
        if user is not None:
            login(request, user)
            return redirect('index')
    
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
    