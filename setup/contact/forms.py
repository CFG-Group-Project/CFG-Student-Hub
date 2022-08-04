from django import forms
from django.forms import ModelForm
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['subject', 'content']