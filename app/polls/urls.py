from django.urls import path

# Import our response 
from . import views


urlpatterns = [
    # Here we are adding our paths or routes
    path("", views.index, name="index"),
    
    # This is an example of how we can receive variables throught the urls
    path("<int:question_id>/", views.detail, name="detail"),

    # Add the home path
    path('home/', views.home, name='home'),
]
    


