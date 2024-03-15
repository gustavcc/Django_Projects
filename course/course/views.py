from django.shortcuts import render
from .models import Question

def landing(request):
    return render(request, 'course/landing.html')

def dashboard(request):
    return render(request, 'course/dashboard.html')

def questions(request):
    questions = {
        'questions': Question.objects.all()
    }
    return render(request, 'course/questions.html', {'questions': questions})