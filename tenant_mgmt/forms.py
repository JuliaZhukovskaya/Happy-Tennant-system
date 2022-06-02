from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from . import util
from .models import *

class IssueCreateForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if util.is_admin_or_manager(user):
            return
        l = None
        if util.is_employee(user):
            properties = Issue.objects.filter(assignee=user)
        else:
            properties = Property.objects.filter(owner=user)
        choices = []
        for prop in properties:
            choices.append((prop.id, str(prop)),)
        self.fields['related_property'].choices = choices

    class Meta:
        model = Issue
        
        fields = '__all__'
        # widgets = {
        #     'email': forms.EmailField()
        # }
        exclude = ['assigner', 'assignee', 'submitter', 'status']
        # ass exclude in view.py before save/commit
        labels = {
            'title': ('Название'),
            'description': ('Описание'),
            'category': ('Категория'),
            'related_property': ('Жилье'),
            'manager': ('Жилец'),
        }


class PropertyCreateForm(ModelForm):

    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['ownerId']
        
        labels = {
            'name': ('Название'),
            'address': ('Адрес'),
            'owner': ('Владелец'),
            'tenants': ('Жильцы'),
        }

class AddressCreateForm(ModelForm):

    class Meta:
        model = Address
        fields = '__all__'
    
        labels = {
            'street': ('Улица'),
            'apartment': ('Квартира'),
            'city': ('Город'),
            'zipCode': ('Индекс'),
            'country': ('Страна'),
        }

class IssueCategoryCreateForm(ModelForm):

    class Meta:
        model = IssueCategory
        fields = '__all__'
    
        labels = {
            'title': ('Название'),
        }
