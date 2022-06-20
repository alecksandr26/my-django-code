from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Here we define the different parts of our project
def index(request):
    return HttpResponse('Hello world')


def login(request):
    return HttpResponse('This is the login')

