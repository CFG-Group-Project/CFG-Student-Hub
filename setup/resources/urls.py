import sys
sys.path.append('..')

from django.urls import path
from . import views
from django.urls import path, include


app_name = 'resources'

urlpatterns = [
    path('resources/', views.resources, name='resources'),
    path('resources/programs', views.programs, name='programs'),
    path('resources/mynotes',views.usernotes,name='user-sub'),
    path('resources/mynotes/search',views.notes_search,name='user-search'),
    path('resources/mynotes/delete_note/<int:pk>',views.delete_note,name='delete_note'),
    path('resources/mynotes/<int:pk>',views.NotesDetailView.as_view(),name='notes-detail'),
    path('resources/mynotes/update/<int:pk>', views.NotesUpdateView.as_view(), name='notes-update'),
    path('resources/programs/<name>', views.ClassPage, name='class-page'),
    path('resources/create', views.CreateResource.as_view(), name='resource-create'),
    path('resources/update/<int:pk>', views.UpdateResource.as_view(), name='resource-update'),
    path('resources/delete/<int:pk>', views.DeleteResource.as_view(), name='resource-delete'),
    path('resources/lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
    path('resources/admin-dash', views.admin_dash, name='admin-dash'),
    path('', include('resources.cards.urls'))
]
