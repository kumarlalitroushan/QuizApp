from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentCreationForm, TeacherRegistrationForm
from .models import CustomUser


# Create your views here.
def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user_type = 'teacher'
            teacher.save()
            login(request, teacher)
            return redirect('home')
    else:
        form = TeacherRegistrationForm()
    return render(request, 'Users/register_teacher.html', {'form': form})


def create_student(request):
    if not request.user.is_authenticated or request.user.user_type != 'teacher':
        return redirect('login')

    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user_type = 'student'
            student.save()
            return redirect('student_list')
    else:
        form = StudentCreationForm()
    return render(request, 'Users/create_student.html', {'form': form})

