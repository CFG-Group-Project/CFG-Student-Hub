from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, {'template': 'register.html'}, name='register'),
    path('registered/', views.registered, {'template': 'registered.html'}, name='registered'),
    path('login/', views.login, {'template': 'login.html'}, name='login'),
    path('logout/', views.logout, {'template': 'login.html'}, name='logout'),
]
