from django.contrib import admin
from django.urls import path
from app_login import views

urlpatterns = [
    path('',views.cadastro,name='cadastro'),
    path('login/',views.login,name='login'),
    path('admin/',admin.site.urls),
]
