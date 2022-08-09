from django.urls import path
from . import views
from django.urls import path, include


app_name = 'flashcards'

urlpatterns = [
    path('resources/flashcards',views.CardListView.as_view(),name="glossarycards-list"),
    path("resources/flashcards/new",views.CardCreateView.as_view(),name="card-create"),
    path("resources/flashcards/edit/<int:pk>",views.CardUpdateView.as_view(),name="card-update"),
    path("resources/flashcards/box/<int:box_num>",views.BoxView.as_view(),name="box"),
]