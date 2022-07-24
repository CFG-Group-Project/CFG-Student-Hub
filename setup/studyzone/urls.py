from django.urls import path
from . import views

app_name = 'studyzone'

urlpatterns = [
    path('study-zone/', views.study, name='studyzone'),
]
