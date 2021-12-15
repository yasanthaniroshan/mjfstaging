from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.urls import path,include
from . import views
from django.contrib.auth import  views as auth_views
from .forms import LoginForm

urlpatterns  = [
    path('',views.mainsite,name="main"),
    path('login/',views.loginuser,name = "login_user"),
    path('register/',views.registerForm,name="register"),
    path('logout/',auth_views.LogoutView.as_view(next_page = 'main'),name="logout"),
] 