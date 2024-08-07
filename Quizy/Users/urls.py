from django.urls import path
from . import views

urlpatterns = [
    path('register-teacher/', views.register_teacher, name='register_teacher'),
    path('create-student/', views.create_student, name='create_student'),
]
