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
