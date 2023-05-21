# userprofile/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/', views.profile_edit_view, name='edit_profile'),

] 
