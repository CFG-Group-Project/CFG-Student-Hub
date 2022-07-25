from django import forms



class CreateNewResource(forms.Form):
    title = forms.CharField(label="Title", max_length=200)
    week = forms.CharField(label='Week', max_length=3)
    show = forms.BooleanField(label='Is this ready for student view?', required=False)
    prog = forms.CharField(label='Program',max_length=20)