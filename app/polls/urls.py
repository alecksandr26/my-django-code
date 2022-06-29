from django.urls import path

# Import our response 
from . import views

APP_NAME = "polls"


urlpatterns = [
    # Here we are adding our paths or routes
    path("", views.IndexView.as_view(), name="index"),
    
    # This is an example of how we can receive variables throught the urls
    path("<int:question_id>/", views.detail, name="detail"),

    # Add the home path
    path('home/', views.HomeView.as_view(), name='home'),
    
    # To do a vote
    path("<int:question_id>/vote", views.vote, name="vote"),
]
    


