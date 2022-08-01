from django.shortcuts import render, redirect
from . import models
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.views.generic import DetailView, ListView
from django.contrib import messages


# Create your views here.
def resources(request):
    return render(request, 'resources/main.html')


def programs(request):
    return render(request, 'resources/pathways.html')


def notesview(request):
    return render(request, 'resources/user-notes.html')


def usernotes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], content=request.POST['content'],
                          link=request.POST['link'])
            notes.save()
        messages.success(request, "Your notes have been saved!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'resources/user-notes.html', context)


def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return HttpResponseRedirect('/resources/mynotes')


class NotesDetailView(DetailView):
    model = Notes


def ClassPage(request, name=None):
    Program.objects.get(path_code=name)
    lessons = Material.objects.filter(show=True)
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        result_list = []
    else:
        form = SearchForm()
    context = {'search': form,'lessons':lessons}
    return render(request, 'resources/prog-page.html', context)


class LessonDetailView(DetailView):
    model = Material


# https://learndjango.com/tutorials/django-search-tutorial

# def materials(request):
#     material = Material.objects.get(id=id)
#     if material is not None:
#         return render(request, 'resources/material-page.html', {'material': material})
#     else:
#         raise Http404('This lesson is unavailable')

def submit_thanks(request):
    return render(request, 'resources/submit-thanks.html')


def submit(request):
    if request.method == 'POST':
        form = CreateNewResource(request.POST)
        if form.is_valid():
            materials = Material(user=request.user, lesson=request.POST['lesson'],
                                 week=request.POST['week'],
                                 slides=request.POST['code'],
                                 topics=request.POST['topics'],
                                 rectutorial=request.POST['rectutorial'])
            materials.save()
        messages.success(request, f"Your lesson have been saved!")
    else:
        form = CreateNewResource
    context = {'form': form}
    return render(request, 'resources/submit.html', {'form': form})
