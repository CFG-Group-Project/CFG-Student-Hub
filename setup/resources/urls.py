from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('resources/mynotes',views.usernotes,name='user-sub'),
    path('resources/mynotes/delete_note/<int:pk>',views.delete_note,name='delete_note'),
    path('resources/mynotes/<int:pk>',views.NotesDetailView.as_view(),name='notes-detail'),
    path('resources/program/<name>', views.ClassPage, name='class-page'),
    path('resources/submit', views.submit, name='submit'),
    path('resources/submit-thanks', views.submit_thanks, name='submit-thanks'),
    # path('resources/', KnowledgeBank.as_view(),name='material'),
    # path('resources/<Program_name>', ProgBank.as_view(),name='program'),
    # path('resources/<int:bank_id>', views.materials, name='materials'),

]
