from typing import Any
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput,PasswordInput

class UserSignupForm(UserCreationForm):
    username = forms.CharField(label='Username',required=True)
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(required=False)
    
    class Meta():
        model = User
        fields = ['username','first_name','last_name','email']
    
    
    
class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
        