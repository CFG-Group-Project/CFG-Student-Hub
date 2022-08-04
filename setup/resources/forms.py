from django import forms
from django.forms import ModelForm
from .models import *


class CreateNewResource(ModelForm):
    lesson = forms.CharField(label='Lesson Title', max_length=50, )
    topics = forms.CharField(label='Topic', max_length=50, )
    week = forms.CharField(label='Week', max_length=3)
    lesson_slide = forms.URLField(label='Lesson Slides', max_length=200)
    code = forms.CharField(label='Code File Link', max_length=400, required=False)
    show = forms.BooleanField(label='Is this ready for students to view?', initial=False, required=False)
    rectutorial = forms.URLField(label='Recommended Tutorial', max_length=200, required=False)
    program = forms.ModelChoiceField(Program.objects.all())
    class Meta:
        model = Material
        fields = ['lesson', 'topics', 'lesson_slide', 'week', 'code', 'rectutorial', 'program', 'show']


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content', 'link']


class SearchForm(forms.Form):
    text = forms.CharField(max_length=100, label='What would you like to search for?', required=False)
