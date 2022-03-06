from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, "index.html" )
    
    


  
# Create your views here.
def geeks_view(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")
   