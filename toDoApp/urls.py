from django.urls import path
from . import views

# url Patterns for ToDoAPP
urlpatterns = [
    # Path for Home Page
    path('', views.homepage, name="homepage"),
]
