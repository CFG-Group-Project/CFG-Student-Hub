from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('registered/', views.registered, name='registered'),
    path('login_user/', views.login_user, name='login'),
]
