from django import forms
from django.forms import ModelForm
from .models import *


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'link']


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, label='What would you like to search for?', required=False)


class MakeVisible(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['show']
