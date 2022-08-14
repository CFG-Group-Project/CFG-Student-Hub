from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("resources/flashcards", views.FlashHome, name="card-home"),
    path("resources/flashcards/new", views.CardCreateView.as_view(), name="card-create"),
    path("resources/flashcards/edit/<int:pk>", views.CardUpdateView.as_view(), name="card-update"),
]
