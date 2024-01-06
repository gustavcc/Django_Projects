from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, view responsável, nome de referencia (url)
    path('',views.home,name='home'), # name é o nome da url, que irá renderizar um page html
    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
