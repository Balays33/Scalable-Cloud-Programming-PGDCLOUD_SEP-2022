from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
def home(request):
    return HttpResponse("Hello, world. You're at the login index.")
"""


rooms =[
  {'id':1, 'name': 'Let play'},
  {'id':2, 'name': 'Let play something'},
  {'id':3, 'name': 'Let play test '},
]


def home(request):
    context= {'rooms':rooms}
    return render(request, 'base/home.html', context)

def help(request):
    print("help page")
    return render(request, 'base/help.html')
    
    
def room(request, pk):
    print("room page")
    room = None
    if(p == null) {
        print("pk is null")
        pk = 3
    
    print(type(pk))
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context= {'room':room}
    return render(request, 'base/room.html', context) 
