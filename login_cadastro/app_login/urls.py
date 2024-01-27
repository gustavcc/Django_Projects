from django.urls import path
from app_login import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/',views.cadastro, name='cadastro'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard, name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
