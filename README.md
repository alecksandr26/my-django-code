# My Django Code
Just my django code
## Start django project
To starta  django project is very easy you only need to run this.
```
$ django-admin startproject apps-name
```
To run the project you need to execute this command.
```
$ python app/manage.py runserver
```
## Django documentation
[Documentation](https://docs.djangoproject.com/en/4.0/)

## Creating modules or apps
In Django you can create modules or apps to divide your code in different parts, making your project more scalable and organize so to create a new app or module just run these commands.
```
$ cd apps-name
$ python manage.py startapp modules-name
```
Inside of this directory there is going to be a file called `views.py` where we are going to use to create our routes from that view, like this.
```
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Here we define the different parts of our project

def index(request):
    return HttpResponse('Hello world')

```
After adding the response we should edit the file `app-name/urls.py` where we are going to add a new path of our project.
```
"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')) # With this we can add our module to our project
]
```
To finish we are going to create a new file inside of our `module` or `app` called `urls.py` where we are going to define again our routes or paths of our app.
```
from django.urls import path

# Import our response 
from . import views


urlspatters = [
    # Here we are adding our function 
    path("", views.index, name="index")
]
```
