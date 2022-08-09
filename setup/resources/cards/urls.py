from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("resources/flashcards",views.CardListView.as_view(),name="card-list"),
]