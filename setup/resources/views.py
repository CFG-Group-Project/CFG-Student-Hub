from django.shortcuts import render
from .models import Material
from django.http import Http404, HttpResponseRedirect
from .forms import CreateNewResource


# Create your views here.
def resources(request):
    return render(request, 'resources/main.html')


def knowbank(request):
    return render(request, 'resources/bank.html')


def materials(request):
    material = Material.objects.get(id=id)
    if material is not None:
        return render(request, 'resources/material-page.html', {'material': material})
    else:
        raise Http404('This lesson is unavailable')


def submit_thanks(request):
    return render(request, 'resources/submit-thanks.html')


# def submit(request):
#     if request.method == 'POST':
#         form = CreateNewResource(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('resources/submit-thanks.hml')
#         else:
#             pass
#     else:
#         form = CreateNewResource()
#     return render(request, 'resources/submit.html', {'form': form})


def submit(request):
    if request.method == "POST":
        form = CreateNewResource(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            prog = form.cleaned_data['prog']
            week = form.cleaned_data['week']
            show = form.cleaned_data['show']
            sub = Material(title=title, prog=prog, week=week, show=show)
            sub.save()
        else:
            pass
    else:
        form = CreateNewResource()
    return render(request, 'resources/submit.html', {'form': form})