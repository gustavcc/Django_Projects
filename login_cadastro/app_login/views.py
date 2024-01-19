from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def cadastro(request):
    if request.method=='GET':
        error_message = None
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            error_message = 'Usuário já cadastrado. Faça login!'
        else:
            user = User.objects.create_user(username=username,email=email,password=senha)
            user.save()
            return redirect('dashboard')
    
    return render(request, 'app_login/pages/cadastro.html', {'error_message': error_message})

def login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login_auth(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
    else: 
        error_message = None
        
    return render(request, 'app_login/pages/login.html', {'error_message': error_message})

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'app_login/pages/dashboard.html')