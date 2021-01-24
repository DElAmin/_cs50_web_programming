from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse("Hello......, world!")
    return render(request, "hello/index.html")

def brain(request):
    return HttpResponse("Hello......, brain!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}")