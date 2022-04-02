from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
def home(request):
    return HttpResponse("Hello, world. You're at the login index.")
"""


#rooms =[
#  {'id':1, 'name': 'Let play'},
#  {'id':2, 'name': 'Let play something'},
#  {'id':3, 'name': 'Let play test '},
#]


def home(request):
    rooms = Room.objects.all()
    context= {'rooms':rooms}
    return render(request, 'base/home.html', context)

@login_required(login_url='/login/login')
def help(request):
    print("help page")
    return render(request, 'base/help.html')
    
    
def room(request, pk):
    print("room page")
    room =Room.objects.get(id=pk)
    context= {'room':room}
    return render(request, 'base/room.html', context) 


def test(request):
    return HttpResponse("Hello, world. You're at the login index.")
    
    
def welcome(request):
    print("welcome page")
    return render(request, 'base/welcome.html')