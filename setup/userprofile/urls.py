from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('forum/', views.forum),
    path('forum/<int:id>/', views.discussion),
    path('forum/create-post', views.create_post),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)