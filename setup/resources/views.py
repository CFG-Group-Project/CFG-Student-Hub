from django.shortcuts import render
from .models import Material, Program, Notes
from django.http import Http404, HttpResponseRedirect
from .forms import *
from django.views.generic import ListView, DetailView


# Create your views here.
def resources(request):
    return render(request, 'resources/main.html')

def usernotes(request):
    form = NotesForm()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes':notes,'form':form}
    return render(request,'resources/user-resources.html',context)



# def materials(request):
#     material = Material.objects.get(id=id)
#     if material is not None:
#         return render(request, 'resources/material-page.html', {'material': material})
#     else:
#         raise Http404('This lesson is unavailable')

def submit_thanks(request):
    return render(request, 'resources/submit-thanks.html')


def submit(request):
    if request.method == "POST":
        form = CreateNewResource(request.POST)
        if form.is_valid():
            lesson = form.cleaned_data['lesson']
            topic = form.cleaned_data['topic']
            week = form.cleaned_data['week']
            show = form.cleaned_data['show']
            rectutorial = form.cleaned_data['rectutorial']
            sub = Material(lesson=lesson, topic=topic, week=week, show=show, rectutorial=rectutorial)
            sub.save()
            return HttpResponseRedirect('resources/submit-thanks.hml')
        else:
            pass
    else:
        form = CreateNewResource()
    return render(request, 'resources/submit.html', {'form': form})


class KnowledgeBank(ListView):
    model = Material
    template_name = 'material-page.html'

class ProgBank(ListView):
    model = Program
    template_name = 'resources/prog-page.html'
    # proglist = Material.objects.all()
