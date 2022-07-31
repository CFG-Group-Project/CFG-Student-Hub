from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.
# @login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
