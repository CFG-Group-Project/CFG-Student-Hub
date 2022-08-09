from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import random
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model




def FlashHome(request):
    return render(request, 'flashcards/glossarycards_list.html')


class CardListView(ListView):
    model = GlossaryCards
    queryset = GlossaryCards.objects.all().order_by("box", "-date_created")


class CardCreateView(CreateView):
    model = GlossaryCards
    fields = ["question", "answer", "box","approved"]
    success_url = "resources/flashcards/new"

    def form_valid(self, form):
        form.instance.sub_by = self.request.user
        return super().form_valid(form)


class CardUpdateView(CardCreateView, UpdateView):
    success_url = "../../flashcards"


class BoxView(CardListView):
    template_name = "flashcards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return GlossaryCards.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(GlossaryCards, id=form.cleaned_data["card_id"])
            card.move(form.cleaned_data["solved"])

        return redirect(request.META.get("HTTP_REFERER"))
