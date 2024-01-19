from django.urls import path
from app_login import views

urlpatterns = [
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
]
