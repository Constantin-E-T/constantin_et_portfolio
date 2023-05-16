# portfolio/urls.py

from django.urls import path
from . import views
from .views import ProjectIndexView 

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('projects/', ProjectIndexView.as_view(), name='projects'), 
]
