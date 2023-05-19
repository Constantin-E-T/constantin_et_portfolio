# register/urls.py

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='login'), # Changed from login_view to login_request
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register_request, name='register'), # Changed from register_view to register_request
]
