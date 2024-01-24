from django.shortcuts import render
from .models import Cut

def register(request):
    return render(request, 'pages/register.html')