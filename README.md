# My Django Code
Just my django code
## Django documentation
[Documentation](https://docs.djangoproject.com/en/4.0/)

## Table of Contents  
1. [Install django](#install)
2. [Staring new project](#create)
3. [Creating modules](#apps)
4. [Creating Models for ORM](#models)
5. [Shell in django](#shell)
6. [Django admin](#admin)
7. [Views](#views)
8. [Templates in django](#template)

<a name="install" />

## Install django
To Install django you only need to run this command
```
$ pip install django
```

<a name="create" />

## Start django project
To starta  django project is very easy you only need to run this.
```
$ django-admin startproject apps-name
```
To run the project you need to execute this command.
```
$ python app/manage.py runserver
```

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
To create a model is very easy you need to go to the file `modules-name/models.py`, here inside in this file we are going to add our models, models are tables where you can define the attributes of your tables.
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
This is the documentation to create models in django [models](https://docs.djangoproject.com/en/4.0/topics/db/models/).

<a name="shell" />

## Shell
To run an interactive shell in django you only need to run this command.
```
$ python manage.py shell
```
Here you can interact your code and do a lot of things.

<a name="admin" />

## Django admin
In django has some tools to administrate our project and configurate our project from any place to be able to do that we need to create a user from the terminal, just run this command and create your user.
```
$ python manage.py createsuperuser
```
Creating a super user and adding this code to our `modules-name/admin` we are going to be able to manipulate the database from a web interface created by django.
```
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

admin.site.register(Question, Choice)
```
Now you can go to the `/admin` and see the interface to administrate the database.

<a name="views" />

## Creating views
Views are just url that we can create to response requests from the users inside of it we can render html, css files to create these web applications, so for example inside of your `modules-name/views.py` we are going to add these views for example this are mine, as you can see we can import our `modules-name/models.py` to interact with the database and fetch data from the database.
```
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Here I can import the database service whichs is inside of the modules files
from .models import Question, Choice


# Here we define the different parts of our project
def index(request):
    return HttpResponse('This is the principal page of this site')


# Here we can alos receive arguments throught the urls
def detail(request, question_id):
    
    return HttpResponse(f'This is the question {question_id} : "{Question.objects.get(pk=question_id)}"') 
```

<a name="template" />

## Templates in django
Now we creating templates basically a template is an html code that we can render with django to create a frontend of our application, this is so easy, so pay atention, inside of our `module` directory we are going to create a new directory called `templates`, inside of here we are going to create a new directoy with the name of our `module`, so basically at the end we are going to finish with something like this, `modules-name/templates/modules-name`, after that we can create html files, for example we can create the `index.html`, this html files are going to be rendered by `jinja2`, so we can program logic inside of them.
```
<!-- This is an example jinja2 code  -->
{% if list_questions %}
<ul>
{% for question in list_questions %}
<li><a href="/polls/{{ question.id }}">{{ question.question_text }}</a></li>
{% endfor %}
</ul>
{% else %}
<p>No polls available </p>
{% endif %}
```


