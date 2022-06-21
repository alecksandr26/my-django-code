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


# This is a new view or path which we are gonig to render our html file 
def home(request):
    list_questions = Question.objects.all()
    # Here we pass the variables as dict
    return render(request, 'polls/index.html', {
        'list_questions' : list_questions
    })


