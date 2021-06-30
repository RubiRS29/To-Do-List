from django.db import models
from django import forms

from .models import Task

from formLists.models import List

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=150 , widget= forms.TextInput(
        attrs={'class': 'form-control form-title'}
    ) )

    date = forms.DateField(widget= forms.TextInput(
        attrs={'class': 'form-date',
                "type" : "date"
                }
    ) )

    listAdd = forms.ModelChoiceField( queryset = List.objects.all() , required=False , widget= forms.Select(
        attrs={'class': 'select-list'}))
    class Meta:
        model = Task
        fields = ("title" , "date" , "listAdd" )

    
