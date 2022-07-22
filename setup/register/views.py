from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.


def register(request):
    #return render(request, 'pages/register.html')
    return HttpResponse('FFS')
