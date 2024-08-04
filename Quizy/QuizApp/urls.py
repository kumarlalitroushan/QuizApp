from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('home/', views.home, name='home'),
    path('questions/<str:subject_name>/', views.questions_page, name='questions_page'),
]