from django.shortcuts import render

def landing(request):
    return render(request, 'course/landing.html')

def dashboard(request):
    return render(request, 'course/home.html')

def questions(request):
    return render(request, 'course/questions.html')