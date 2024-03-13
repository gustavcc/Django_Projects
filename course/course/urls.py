from django.urls import path
from course import views

urlpatterns = [
    path('', views.landing, name='Landing'),    
    path('dashboard/', views.dashboard, name='Dashboard'),    
    path('questoes/', views.questions, name='Questoes'),    
]