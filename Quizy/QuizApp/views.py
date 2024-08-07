from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Class, Subject, Question
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from .forms import QuestionForm


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


@login_required
def create_question(request):
    if request.user.user_type != 'teacher':
        raise PermissionDenied("You do not have permission to add questions.")

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.teacher = request.user
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'QuizApp/create_question.html', context)
