from django.shortcuts import render
from .models import Usuario

#! função que define a lógica que será feita (abrir page html)
def home(request):
    return render(request,'usuarios/home.html')

#! chama / salva as propriedades do formulario (nomes)
def usuarios(request):
    
    #! salvar dados da tela para o db (salvar dados - POST)
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    #! exibir todos os usuarios em uma nova pagina (Django interpreta em dicionario)
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    #! retornar os dados para a pagina de listagem
    return render(request,'usuarios/listagem_usuarios.html',usuarios)