from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Class, Subject, Question


def login_page(request):
    return render(request, 'QuizApp/loginpage.html')


def home(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        print(subject, '>>>>>>>>>>>>>>>>>>>>>>>')
        # Redirect to questions_page with subject as a URL parameter
        return redirect(reverse('questions_page', kwargs={'subject_name': subject}))
    return render(request, 'QuizApp/home.html')


def questions_page(request, subject_name):
    class_obj = get_object_or_404(Class, name='Class 1')
    subject_obj = get_object_or_404(Subject, name=subject_name)

    # This will query all questions related to class and subject selected
    questions = Question.objects.filter(class_name=class_obj, subject=subject_obj)

    context = {
        'class': class_obj,
        'subject': subject_name,
        'questions': questions,
    }
    return render(request, 'QuizApp/questionsPage.html', context)
