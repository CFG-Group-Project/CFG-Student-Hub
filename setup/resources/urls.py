from django.urls import path
from . import views
from .views import KnowledgeBank, ProgBank

app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('resources/submit', views.submit, name='submit'),
    path('resources/submit-thanks', views.submit_thanks, name='submit-thanks'),
    # path('resources/', KnowledgeBank.as_view(),name='material'),
    path('resources/<Program_name>', ProgBank.as_view(),name='program')
    # path('resources/<int:bank_id>', views.materials, name='materials')
]
