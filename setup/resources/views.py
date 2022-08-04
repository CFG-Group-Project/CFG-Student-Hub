from django.shortcuts import render, redirect
from . import models
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required(login_url='/login/')
def resources(request):
    return render(request, 'resources/main.html')


@login_required(login_url='/login/')
def notesview(request):
    return render(request, 'resources/user-notes.html')


@login_required(login_url='/login/')
def usernotes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(user=request.user, title=request.POST['title'], content=request.POST['content'],
                          link=request.POST['link'])
            notes.save()
            form = NotesForm()
        messages.success(request, "Your notes have been saved!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'resources/user-notes.html', context)

def notes_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        notes = Notes.objects.filter(content__contains=searched)
        context = {'searched':searched,'notes':notes}
        return render(request, 'resources/notes-search.html',context)
    else:
        return render(request, 'resources/notes-search.html', {})

@login_required(login_url='/login/')
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return HttpResponseRedirect('/resources/mynotes')


class NotesDetailView(DetailView):
    model = Notes


@login_required(login_url='/login/')
def programs(request):
    return render(request, 'resources/pathways.html')


@login_required(login_url='/login/')
def ClassPage(request, name=None):
    lessons = Material.objects.filter(show=True, program=name)
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        result_list = []
    else:
        form = SearchForm()
    context = {'search': form, 'lessons': lessons}
    return render(request, 'resources/prog-page.html', context)


class LessonDetailView(DetailView):
    model = Material


class FoundationDetailView(DetailView):
    model = Material


# https://learndjango.com/tutorials/django-search-tutorial

# def materials(request):
#     material = Material.objects.get(id=id)
#     if material is not None:
#         return render(request, 'resources/material_detail.html', {'material': material})
#     else:
#         raise Http404('This lesson is unavailable')

@login_required(login_url='/login/')
def submit_thanks(request):
    return render(request, 'resources/submit-thanks.html')


@login_required(login_url='/login/')
def submit(request):
    if request.method == 'POST':
        form = CreateNewResource(request.POST)
        if form.is_valid():
            materials = Material(lesson=request.POST['lesson'], week=request.POST['week'],
                                 slides=request.POST['code'],
                                 topics=request.POST['topics'],
                                 program='program',
                                 show='show',
                                 rectutorial=request.POST['rectutorial'])
            materials.save()
        messages.success(request, f"Your lesson has been saved!")
    else:
        form = CreateNewResource
    context = {'form': form}
    return render(request, 'resources/submit.html', {'form': form})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff)
def admin_dash(request):
    dashcon = Material.objects.all()
    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
        for x in id_list:
            if Material.objects.filter(pk=int(x)):
                Material.objects.filter(pk=int(x)).update(show=True)
            elif not Material.objects.filter(pk=int(x)):
                Material.objects.filter(pk=int(x)).update(show=False)
        messages.success(request,"The selected lessons have been updated")
        return render(request, 'resources/admindash.html', {'dashcon': dashcon})
    else:
        return render(request, 'resources/admindash.html', {'dashcon': dashcon})



# currently, the student accounts redirect to a 404 page. this might be rectified by Ayisha's 404 redirect API but remember to check

