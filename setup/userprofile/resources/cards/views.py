from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
import random
from django.contrib.messages.views import SuccessMessageMixin
from .models import Card
from .filters import *
from django.contrib.auth.decorators import login_required


def FlashHome(request):
    cards = Card.objects.filter(approved=True)
    myFilter = TopicFilter(request.GET, queryset=cards)
    cards = myFilter.qs
    return render(request, 'cards/flashcards.html', {'cards': cards,'myfilter':myFilter})


class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by("-date_created")


class CardCreateView(CreateView,SuccessMessageMixin):
    model = Card
    fields = ["question", "answer", "topic"]
    success_url = reverse_lazy("card-create")
    success_message = "Your message was successfully. It will be visible once it is approved."

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.calculated_field,
        )

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.program = self.request.user.profile.stream
        return super().form_valid(form)



class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

