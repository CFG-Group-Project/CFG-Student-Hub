from django.shortcuts import render
from . import views

# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html')