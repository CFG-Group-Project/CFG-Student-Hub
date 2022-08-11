from django.shortcuts import render, redirect
from .models import Material,Program,Notes
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import DetailView, ListView
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
from .filters import MaterialFilter,MaterialFilterStudents



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
                          link=request.POST['link']).order_by('title')
            notes.save()
            form = NotesForm()
        messages.success(request, "Your notes have been saved!")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(user=request.user).order_by('title')
    context = {'notes': notes, 'form': form}
    return render(request, 'resources/user-notes.html', context)


def notes_search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        # searches title and content but only for current user
        notes = Notes.objects.filter(Q(title__contains=searched) | Q(content__contains=searched)).filter(
            user=request.user)
        context = {'searched': searched, 'notes': notes}
        return render(request, 'resources/notes-search.html', context)
    else:
        return render(request, 'resources/notes-search.html', {})


@login_required(login_url='/login/')
def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return HttpResponseRedirect('/resources/mynotes')


class NotesDetailView(DetailView):
    model = Notes

class NotesUpdateView(UpdateView):
    model = Notes
    fields = ['title','content','link']
    success_url = '/resources/mynotes'


@login_required(login_url='/login/')
def programs(request):
    return render(request, 'resources/pathways.html')


@login_required(login_url='/login/')
def ClassPage(request, name=None):
    fnd = 'Foundation'
    lessons = Material.objects.filter(show=True).filter(Q(program=name) | Q(program=fnd))
    myFilter = MaterialFilterStudents(request.GET, queryset=lessons)
    lessons = myFilter.qs
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = request.POST['text']
        result_list = []
    else:
        form = SearchForm()
    context = {'search': form, 'lessons': lessons,'myfilter':myFilter}
    return render(request, 'resources/prog-page.html', context)


class LessonDetailView(DetailView):
    model = Material


@login_required(login_url='/login/')
def submit_thanks(request):
    return render(request, 'resources/submit-thanks.html')


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff)
def admin_dash(request):
    dashcon = Material.objects.all().order_by('week')
    myFilter = MaterialFilter(request.GET, queryset=dashcon)
    dashcon= myFilter.qs
    if request.method == 'POST':
        id_list = request.POST.getlist('boxes')
        for x in id_list:
            if Material.objects.filter(pk=int(x)):
                Material.objects.filter(pk=int(x)).update(show=True)
            elif not Material.objects.filter(pk=int(x)):
                Material.objects.filter(pk=int(x)).update(show=False)
        messages.success(request, "The selected lessons have been updated")
        return render(request, 'resources/admindash.html', {'dashcon': dashcon})
    else:
        return render(request, 'resources/admindash.html', {'dashcon': dashcon,'myfilter':myFilter})


# https://youtu.be/llbtoQTt4qw?t=2785 update and create options for the dashboard

# currently, the student accounts redirect to a 404 page. this might be rectified by Ayisha's 404 redirect API but remember to check


class CreateResource(CreateView):
    model = Material
    fields = ['lesson','week','slides','code_file','show','topics','program','rectutorial']
    success_url = '/resources/admin-dash'

    def form_valid(self, form):
        form.instance.sub_by = self.request.user
        return super().form_valid(form)



class UpdateResource(UpdateView):
    model = Material
    fields = ['lesson','week','slides','code_file','show','topics','program','rectutorial']
    success_url = '/resources/admin-dash'

class DeleteResource(DeleteView):
    model = Material
    fields = ['lesson','week','slides','code_file','show','topics','program','rectutorial']
    context_object_name = 'material'
    success_url = '/resources/admin-dash'


