from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages  # In built flash messages for the user


# views
def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            print('worked')
            return redirect('/accounts/registered')
        else:
            error = form.errors.as_data()
            print(form.errors)
            messages.success(request, error)
            form = NewUserForm()
            print('didnt work')


    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def registered(request):
    pass
    context = {}
    return render(request, 'authentication/registered.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Email or password incorrect. Please try again.')
            return redirect('/accounts/login_user')
    context = {}
    return render(request, 'authentication/login.html', context)


