from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('resources/knowledge-bank/',views.knowbank,name='knowledge-bank'),
    path('resources/submit',views.submit,name='submit'),
    path('resources/submit-thanks', views.submit_thanks, name='submit-thanks'),
    path('resources/<int:bank_id>',views.materials, name='materials')
]
