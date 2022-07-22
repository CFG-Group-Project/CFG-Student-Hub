from django.shortcuts import render
from .forms import NewUserForm


#from .forms import NewUserForm

from django.http import HttpResponse


# Create your views here.
def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'pages/register.html', context)


def login(request):
    return render(request, 'pages/login.html')
