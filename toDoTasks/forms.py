from django.db import models
from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=150 ,widget= forms.TextInput(
        attrs={'class': 'form-control form-title'}
    ) )

    date = forms.DateField(widget= forms.TextInput(
        attrs={'class': 'form-date',
                "type" : "date"
                }
    ) )

    listAdd = forms.CharField(max_length=150 ,widget= forms.TextInput(
        attrs={'class': 'select-list'}
    ) )

    class Meta:
        model = Task
        fields = ("title" , "date" , "listAdd" )

    
