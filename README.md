# My Django Code
Just my django code
##### Table of Contents  
1. [Creating modules](#apps)
2. [Creating Models for ORM](#models)
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
<a name="apps" />
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
    path('', include('polls.urls')) # With this we can add our module to our project
]
```
To finish we are going to create a new file inside of our `module` or `app` called `urls.py` where we are going to define again our routes or paths of our app.
```
from django.urls import path

# Import our response 
from . import views


urlpatterns = [
    # Here we are adding our function 
    path("", views.index, name="index")
]
```
<a name="models" />

## Creating Models
To create a model is very easy you need to go to the file `app-name/models.py`, here inside in this file we are going to add our models, models are tables where you can define what tables are you going to create and use everything from django.
```
from django.db import models

# Create your models here.

# This is how we can create a new table inside of our table
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date publish")

# This is another table 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
This is not all to load these chagnes and connect this things to our project we need to add this thing inside of our config file where we can find it here, `apps-name/settings.py`, inside of this file we just add this string to the list `INSTALLED_APPS`.
```
# Application definition

INSTALLED_APPS = [
    "apps-name.apps.apps-nameConfig", # We add something like this 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
With this we only need to run a simple these commands which is going to make our changes and things to the database that we selected before.
```
$ python manage.py makemigrations apps-name
$ python manage.py migrate
```
