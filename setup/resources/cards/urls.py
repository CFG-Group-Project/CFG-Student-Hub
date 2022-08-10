from django.urls import path
# Removed: from django.views.generic import TemplateView

from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path("resources/flashcards", views.FlashHome, name="card-home"),
    path("resources/flashcards/list",views.CardListView.as_view(),name="card-list"),
    path("resources/flashcards/new",views.CardCreateView.as_view(),name="card-create"),
    path("resources/flashcards/edit/<int:pk>",views.CardUpdateView.as_view(),name="card-update"),
    path("resources/flashcards/box/<int:topic>",views.TopicView.as_view(),name="topic"),
]
