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

## Creating modules
In Django you can create modules or apps to divide your code in different parts, making your project more scalable and organize so to create a new app or module just run these commands.
```
$ cd apps-name
$ python manage.py startapp modules-name
```
Inside of this directory there is going to be a file called `views.py` where we are going to use to create our routes.
```
from django.shortcuts import render

# Create your views here.

```
