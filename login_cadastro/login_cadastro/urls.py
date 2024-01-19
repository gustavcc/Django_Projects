from django.contrib import admin
from django.urls import path
from app_login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.cadastro, name='cadastro'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
] 
