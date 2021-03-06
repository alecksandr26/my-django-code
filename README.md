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
9. [Error 404](#error404)
10. [Forms](#forms)
11. [Class Based Views](#classviews)
12. [Testing](#test)
13. [Static in django](#static)
14. [Django Admin part 2](#djangoadmin)
15. [Database](#database)

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
Here you can interact your code and do a lot of things, here is the documentation [shell](https://docs.djangoproject.com/en/4.0/ref/django-admin/#shell).

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
To render this code with the variables we need to add a function like this into our `views.py`  and yeah is acutally quite easy.
```
# This is a new view or path which we are gonig to render our html file 
def home(request):
    list_questions = Question.objects.all()
    # Here we pass the variables as dict
    return render(request, 'polls/index.html', {
        'list_questions' : list_questions
    })
```
And just add that function to our `urls.py` module.
```
urlpatterns = [
    # Here we are adding our paths or routes
    path("", views.index, name="index"),
    
    # This is an example of how we can receive variables throught the urls
    path("<int:question_id>/", views.detail, name="detail"),

    # Add the home path
    path('home/', views.home, name='home'),
]
```

<a name="error404" />

## Error 404
Sometimes the users are going to request some data that we don't have and to avoid errors when we were featching that data and get an error from the data base we can use a function to get an 404 error and return that, just like this we can avoid errors inside of our view.
```
# Here we can alos receive arguments throught the urls
def detail(request, question_id):
    # If the object doens't exist django return 404 for us
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/detail.html', {
        'question' : question,
        'number' : question_id
    })
```
This is the `ditail.html`.
```
<p>Question: {{ question }}</p>
<p>Question number: {{ number }}</p>
```

<a name="forms" />

## Forms
This is the way how we can start creating interfaces that we can use to capture data from the user and start creating an interactive project, for example I rewrite the `detail.html` file to create a form  so take a look with this thing, the important thing here is the tag `csrf_token` this is a tag which help us to avoid cross side scripting and other vulneravilitys to our forms.
```
<form action="{% url 'vote' question.id %}" method="post">
    <!-- For security purpuse -->
    {% csrf_token %}
    <fieldset>
        <legend><h1>{{ question }}</h1></legend>
        <!-- if there is an erro show the error -->
        {% if error_message %}
        <p><strong>{{ error_message }}</strong></p>
        {% endif %}



        <!-- Iterate in all the choices  -->
        {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}"/>
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label>
        <br />
        <!-- Print the number of votes -->
        <p>Votes: {{ choice.votes }}</p>
        <br />

        {% endfor %}
    </fieldset>
    <!-- Send the post  -->
    <input type="submit" value="votar"/>
</form>
```
If you read this `html` code basically we are doing a `post` request to the url `question_id/vote` so in this example I'm going to create another view which will contain that route or path, basically this is the view, inside of this function as you can see we can use the received objected called `request` we can use this object to get the data from the `post` and deal with them to do a query to our database.
```
# Receive only posts
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # With request.POST we can get the data from the from the post 
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            'question' : question,
            'error_message' : "You don't selected a correct answer"
        })
    else:
        # If everything is okay increase the value and redirect again to detail
        selected_choice.votes += 1;
        selected_choice.save()

        return HttpResponseRedirect(reverse("detail", args=(question_id, )))
```
As you can see we can use `HttpResponseRedirect` and `reverse` to redirect the user to another view very simple right.

<a name="classviews" />

## Class Based Views
Basically the class based views is the way how we can create views by creating and using classes in python `OOP` in another words there is a documentation of django where whe can find some of the this classes already created by django we only need to inherit them and work with them, this is the documentation [documentation](http://ccbv.co.uk/) and this is an example basically I modigy my `views.py` to replace the functions `detail`, `home` to a only one view.
```
from django.views import generic

# Here we define the different parts of our project
# def index(request):
#     return render(request, 'polls/index.html')

# This is a class based view
class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
```
With that simple code I'm replacing that function to a simple object the last thing to do to create this `class view` we only need to modify our `modules-name/urls.py` and just our class view, like this just execute the method `as_view`.
```
    # This is how we can add our class view to the urls list
    path("", views.IndexView.as_view(), name="index"),
```
And just like that this thing works, but now what happens in those `views` where I do query requests, well in those cases we need to `inherit` other `Views` from the `generic.py`, so basically lets see for example of the class view of my function `home`, you need to declare specifyc this attributes and functions otherwise your are going to get an error.
```
# This is a new view or path which we are gonig to render our html file 
# def home(request):
#     list_questions = Question.objects.all()
    
#     # Here we pass the variables as dict
#     return render(request, 'polls/home.html', {
#         'list_questions' : list_questions
#     })


class HomeView(generic.ListView):
    model = Question
    template_name = 'polls/home.html'
```
So yeah as you can see with a few lines of code we can do the same thing, but this is not all we need to modify our `template` that we were rendering because the in the contex of this view that is going to use will contain `object_list` instead of `list_questions`.
```
<!-- This is an example jinja2 code  -->
<h1>Questions: </h1>
{% if object_list %}
<ul>
    {% for question in object_list %}
    <!-- To avoid hard coding we can use the url function of jinja2 -->
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
</ul>
{% else %}
<p><strong>No questions available...</strong></p>
{% endif %}
```

<a name="test" />

## Testing
Its important to test our code all the time, every module or functionality that we created inside of our code must be tested, so inside of django we have a complete module for testing, so lets create a file called `test.py` inside of the module and inside of them put all this code.
```
from django.test import TestCase

class QuestionModelTests(TestCase):
    pass
```
Inside of this testacase we can test `models` and `views` to check if they works, so for example to create a new test we only need to create a function inside of this class which must to starts with `test_` and after that you can put any name, then these are my tests.
```
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
import datetime
from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recetly_with_future_questions(self):
        """Test the Questions model"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Quien es el mejor course director", pub_date=time)
        
        # Do a simple assert and check if this is an error
        self.assertIs(future_question.was_recent(), False)


    def test_was_now_questions(self):
        """Test this questions"""
        time = timezone.now()
        now_question = Question(question_text = "Is this recent?", pub_date=time)
        self.assertIs(now_question.was_recent(), True)


    def test_wasnt_recent_question(self):
        """Test old questions"""

        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(question_text = "Is this an old question?", pub_date = time)
        self.assertIs(old_question.was_recent(), False)
```
To run the tests is very easy just put the command test and the name of the module.
```
$ python manage.py test modules-name
```
Now lets create another testcase where we test one of our `views`.
```
from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
import datetime
from .models import Question


class HomeViewTests(TestCase):
    def test_no_questions(self):
        """if no questions exist, an appropiet message is displayed"""
        response = self.client.get(reverse("home"))
        # Test the response code
        self.assertEqual(response.status_code, 200)

        # Test that we don't have question
        self.assertQuerysetEqual(response.context['object_list'], [])


    def test_questions_not_empty(self):
        """Testing question with future"""
        time = timezone.now()
        future_question = Question(question_text = "This is a test question for the future", pub_date = time)
        future_question.save()
        
        response = self.client.get(reverse('home'))
        self.assertNotEqual([], response.context['object_list'])
```
And we can create more and more tests if you want to make sure that your application works.

<a name="static" />

## Static in django
Let's see how we can create the static files in django to add render things inside of our code, firstly we need to add into our module directoy a new directory called `static` inside of here we can add another direcotry call `polls` to avoid confusion and now yeah here we can add our `.css` files, now to add this css file to one of our projects is quite simple only run this tag and add this thing here.
```
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}" />


<!-- This is the main page--->
<h1>Questions?...</h1>

<p>Do you want to vote?: <a href="{% url 'home' %}">Questions</a></p>
```
You see simple right?, just run the tag `load static` and with that we are ready to include all the `.css` files that we want, so for example this is my `.css` files I called `style.css`.
```
h1 {
    color: red;
}


li a {
    color: green;
}
```
So lets put this tyle to another `.html` file, for exmaple this.
```
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}" />

<!-- This is an example jinja2 code  -->
<h1>Questions: </h1>
{% if object_list %}
<ul>
    {% for question in object_list %}
    <!-- To avoid hard coding we can use the url function of jinja2 -->
    <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
</ul>
{% else %}
<p><strong>No questions available...</strong></p>
{% endif %}
```
And if nothing changes just re run the server and you will notice the chagne, now lets see how to put images into our project with django is very simple and easy you only need to create a folder called iamges inside of your `static` folder and from the `.css` file you are going to include that image just like this.
```
h1 {
    color: red;
}


li a {
    color: green;
}

body {
    background: white url("images/background.gif");
}
```
If doen't work I recommend to your to put change this setting `settings.py` variable to set the correct static files.
```
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/polls/'
```
And just like that you can add static files like images to your porject.


<a name="djangoadmin" />

## Django Admin part 2
We can add more functionalitys to the interface of django admin to administrate and test better our application creating new elements and filtring in a better way the data from our database so lets see, first the file where we are going to add these functionalitys is the `admin.py` this file will be in your module or app that you were creating, so now inside of this `.py` file we can give to the django different configuratons and functions that we want to apply or have inside of our django administator page.
```
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```
For example I add a new functionality, now when I want to edit or create a new `Question` basically I'will be able to edit or define the fields in that order, so take a look.<br />
![image](https://user-images.githubusercontent.com/66882463/175752178-892f0ca2-b478-4e0f-8c57-50e344449ee4.png) <br />
So now for example imagine that I want to be able to add choices to the questions from the django administartor, this is easy we only need to create a new class just like this.
```
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```
As you can see is very simple we only need to declare and object with an inheritance of `StackedInline` inside of that class we define the model and the field `extra` refes of the amount that we want of that kind of object or table, and inside of our `ModelAdmin` we can add our choice class int he field of `inlines`, so yeah take look. <br />
![image](https://user-images.githubusercontent.com/66882463/175752393-2474e40d-cf42-44c3-90b4-8104e10544d3.png) <br />
Now I can add choices to the questions everything from the interface of django admin, now lets see how we can present better our questions, we can add a field to our `QuestionAdmin` class where we decid how eacho question will be show it, this field is `list_diesplay`.
```
class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_recent")
```
Now to filter our questions we can add new field where we can put the variables can be filter and depending on type the methods of searching are going to change, so take look.
```
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_recent")
    list_filter = ["pub_date", "question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```
Here at the `list_filter` I put the variables that I want to search and this is the result take look. <br />
![image](https://user-images.githubusercontent.com/66882463/175752840-658d8852-01d5-4c40-ae9a-0f280d76ba8e.png) <br  />
And what django do with the variable text is agroup the questions with the same `question_text`, so to actually search by the name or `question_text` variable we can add another field take look.
```
from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_recent")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
```
Now with the field `search_fields` we can seach by the question name and no by selecting by groups so just take a look. <br />
![image](https://user-images.githubusercontent.com/66882463/175752960-ac6acdb4-49fd-4d04-aab8-45eec8f27e34.png)<br />
We can filter all the questions thats incredible right?, then this is the documentation if you want to search more settings that we can define to our django admin [documentation](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/).

<a name="database" />

## Database
At end of this little script, to connect to an external databse server is quite simple you only need to edit the variable `DATABASE` in `settings.py` and with that we are going to be able to connect our project to our external server database, so just add something like this.
```
# This is en example of how to connect to an external database 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'personalweb',     # The name of the database
        'USER' : 'remote',      # The username to log into the database
        'PASSWORD' : '2346rsdf34t2', # The password of the username
        'HOST' : '192.168.100.150', # The ip address of the host
        'PORT' : '3306'    # And the port where myslq is running
    }
}
```
Then at the end just run this command to connect and let django to configure somethings.
```
$ python manage.py migrate
```
If you are using `mysql` and you get an erro you need to install the package of `msqlclient` and yeath thats it.


