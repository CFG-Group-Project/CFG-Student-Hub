from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


# Create your forms here.
class NewUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'enter your username',
            'maxlength': 16,
            'minlength': 5
        })

        self.fields['email'].widget.attrs.update({
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'enter your email address',
            'maxlength': 255,
            'minlength': 5

        })

        self.fields['password1'].widget.attrs.update({
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'enter your password',
            'maxlength': 255,
            'minlength': 3

        })

        self.fields['password2'].widget.attrs.update({
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'enter your password',
            'maxlength': 255,
            'minlength': 3

        })

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


