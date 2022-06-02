from dataclasses import field
from distutils.command.build_scripts import first_line_re
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Ваше имя', max_length=100)
    last_name = forms.CharField(label='Ваша фамилия', max_length=100)
  
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='Ваше имя', max_length=100)
    last_name = forms.CharField(label='Ваша фамилия', max_length=100)
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['picture']