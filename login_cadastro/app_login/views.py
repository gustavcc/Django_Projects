from django.shortcuts import render
from .models import Usuario

# Create your views here.

def cadastro(request):
    return render(request, 'app_login/index.html')

def login(request):
    pass