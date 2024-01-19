from django.shortcuts import render
from .models import Usuario

# Create your views here.

def cadastro(request):
    return render(request, 'app_login/pages/index.html')

def login(request):
    return render(request, 'app_login/pages/login.html')

def dashboard(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.senha = request.POST.get('senha')
    novo_usuario.save()
    #! exibir todos os usuarios em uma nova pagina (Django interpreta em dicionario)
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #! retornar os dados para a pagina de listagem
    return render(request,'app_login/pages/dashboard.html',usuarios)