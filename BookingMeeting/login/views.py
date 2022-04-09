from django.shortcuts import render, redirect
from django.contrib import messages                             # django flash messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout   #user autheticate
from django.contrib.auth.decorators import login_required     # user  wants to acces a page
#from .forms import CustomUserCreationForm                     # user registration form
#from django.contrib.auth.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .forms import UpdateUserForm


#from .forms import UpdateUserForm, UpdateProfileForm
from django.views import View
from .forms import RegisterForm

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
    
    

#login page view
def loginUser(request):
    print('login page')
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username'].lower()
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

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration')
    
    return render(request, 'login/login_register.html', {'page': page, 'form': form})
    
     
    
#registration page view
def user_profile(request, pk):
    print("user_profile page")
    context = {}   
    if request.method == 'POST':
        useremail = request.POST['email'].lower()
        print('useremail',useremail)
    try:
        user = User.objects.get(email=useremail)
        user.save()
    except:
        messages.error(request, 'User does not exist')
        print('ERROR')
        
    else:
        print("Nothing went wrong")
        
    return render(request, "login/user_profile.html", context )
    


#test page view
@login_required(login_url='login')
def test(request):
    print("test page")
    
    return render(request, "login/test.html" )
    
    
    
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'login/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
