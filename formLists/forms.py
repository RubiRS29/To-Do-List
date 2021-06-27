from django.db import models
from django import forms

from .models import List


class ListForm(forms.ModelForm):
    title = forms.CharField(max_length=150 ,widget= forms.TextInput(
        attrs={'class': 'form-control form-title'}
    ) )

    class Meta:
        model = List
        fields = ( "title" , )

    