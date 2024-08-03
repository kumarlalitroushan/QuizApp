from django.shortcuts import render

# Create your views here.

def login_page(request):
    return render(request, 'QuizApp/loginpage.html')

def home(request):
    return render(request, 'QuizApp/home.html')