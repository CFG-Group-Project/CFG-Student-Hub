from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('knowledge-bank/',views.knowbank,name='knowledge-bank')
]
