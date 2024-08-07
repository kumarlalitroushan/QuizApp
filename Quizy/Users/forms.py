from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student


class TeacherRegistrationForm(UserCreationForm):
    user_id = forms.CharField(max_length=10)
    emp_id = forms.CharField(max_length=5)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('user_id', 'emp_id', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'teacher'
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    user_id = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'enrollment_id', 'student_class', 'roll_number', 'dob']

    def save(self, commit=True):
        student = super().save(commit=False)
        if commit:
            student.save()
        return student
