from django.urls import path

# Import our response 
from . import views


urlpatterns = [
    # Here we are adding our paths or routes
    path("", views.index, name="index")
]
    


