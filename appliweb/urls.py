from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('services', views.services, name='services'),
    path('propos', views.propos, name= 'propos'),
] 

