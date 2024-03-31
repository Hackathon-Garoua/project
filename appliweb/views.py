from django.contrib.auth import login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def propos(request):
    return render(request, 'propos.html')