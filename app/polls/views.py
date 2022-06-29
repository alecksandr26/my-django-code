from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Here I can import the database service whichs is inside of the modules files
from .models import Question, Choice



# Here we define the different parts of our project
# def index(request):
#     return render(request, 'polls/index.html')


# This is a class based view
class IndexView(generic.TemplateView):
    template_name = 'polls/index.html'
    

# Here we can alos receive arguments throught the urls
def detail(request, question_id):
    # If the object doens't exist django return 404 for us
    question = get_object_or_404(Question, pk=question_id)
    
    return render(request, 'polls/detail.html', {
        'question' : question,
        'number' : question_id
    })


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


