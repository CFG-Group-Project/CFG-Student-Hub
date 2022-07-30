from django.urls import path, include
from . import views

app_name = 'forum'

urlpatterns = [
    path('forum/', views.forum, name='forum'),
    path('forum/<int:id>/', views.discussion, name='forum'),
    path('forum/create-post', views.create_post, name='forum'),
]
