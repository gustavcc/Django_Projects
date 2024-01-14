from django.contrib import admin
from django.urls import path
from paginas import views

urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.cortes,name='dashboard'),
    path('admin/', admin.site.urls),
]