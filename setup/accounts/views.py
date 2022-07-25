from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages, auth  # In built flash messages for the user


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
            errors = form.errors.as_data()
            for k, v in errors.items():
                error = str(v[0]).strip("['']")

                # Only printing one error
                messages.success(request, error)
            form = NewUserForm()

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def registered(request):
    pass
    context = {}
    return render(request, 'accounts/registered.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, 'Email or password entered incorrectly. Please try again.')
            return redirect('/accounts/login')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('accounts/login')
