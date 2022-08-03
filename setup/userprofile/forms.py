from django import forms

from .models import Profile
from .models import Post


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    username = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'title',
            'type': 'text',
            'placeholder': 'enter title of post',
            'maxlength': 200,
        })
        self.fields['content'].widget.attrs.update({
            'required': '',
            'name': 'username',
            'id': 'content',
            'class': 'content',
            'type': 'text',
            'placeholder': 'What would you like to ask?',
            'minlength': 5
        })
        self.fields['categories'].widget.attrs.update({
            'required': '',
            'name': 'categories',
            'id': 'categories',
            'type': 'text',
            'maxlength': 16,
            'minlength': 5
        })
    class Meta:
        model = Post
        fields = ["title", "content", "categories"]
