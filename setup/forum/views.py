from django.shortcuts import render
from . import views

# Create your views here.
def forum(request):
    return render(request, 'forum/forum.html')


def discussion(request):
    return render(request, 'forum/discussion.html')


def create_post(request):
    return render(request, 'forum/create_post.html')

