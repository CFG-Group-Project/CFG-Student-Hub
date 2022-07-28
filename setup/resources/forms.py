from django import forms
from django.forms import ModelForm
from .models import Material


class CreateNewResource(ModelForm):
    lesson = forms.CharField(label='Lesson Title', max_length=50)
    topic = forms.CharField(label='Topic', max_length=50)
    week = forms.CharField(label='Week', max_length=3)
    slides = forms.FileField(label='Lesson Slide', max_length=None, allow_empty_file=False)
    show = forms.BooleanField(label='Is this ready for study view?',initial=False,required=False)
    rectutorial = forms.URLField(label='Recommended Tutorial', max_length=200,required=False)

    class Meta:
        model = Material
        fields = ['lesson', 'topic', 'week', 'slides', 'show', 'rectutorial']


