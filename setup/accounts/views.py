from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from .forms import NewUserForm

from django.http import HttpResponse, HttpResponseRedirect


# views
def register(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'pages/register.html', context)


def login_page(request):
    # obtains the context for the user's request
    context = RequestContext(request)
    if request.method == 'POST':
        # username and password provided by the user.
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('register')
            print('WORKED')
        else:
            print(f'{user}')

    context = {}
    return render(request, 'pages/login.html', context)
