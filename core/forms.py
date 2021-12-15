from django import forms
from django.forms import fields, widgets
from .models import User
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
      "placeholder":"Username",
      "class":"form-control",
      "autofocus" : True,
  }))
  password = forms.CharField(widget = forms.PasswordInput(attrs={
      "placeholder":"Password",
      "Class":"form-control",
  }))
class Usercreationform(UserCreationForm):
    class Meta:
        model = User
        fields =  ("username",)
        
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Username",
        "class":"form-control",
        "autofocus" : True,
        "required":True,
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder":"Your email",
        "Class":"form-control",
    }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        "placeholder":"Password",
        "class":"form-control",
    }))
    password_confirmation = forms.CharField(widget = forms.PasswordInput(attrs={
        "placeholder":"Password",
        "class":"form-control",
    }))