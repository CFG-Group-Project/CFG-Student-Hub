from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import random
from .models import Card
from .filters import *


def FlashHome(request):
    cards = Card.objects.filter(approved=True)
    myFilter = TopicFilter(request.GET, queryset=cards)
    cards = myFilter.qs
    return render(request, 'cards/flashcards.html', {'cards': cards,'myfilter':myFilter})


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("-date_created")


class CardCreateView(CreateView):
    model = Card
    fields = ["question", "answer", "topic"]
    success_url = reverse_lazy("card-create")


class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")


class TopicView(CardListView):
    template_name = 'cards/topic.html'

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context