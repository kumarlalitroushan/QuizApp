from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Class(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='questions')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f"{self.subject.name}: {self.question_text[:50]}..."

    def clean(self):
        if self.answer not in [self.option1, self.option2, self.option3, self.option4]:
            raise ValidationError('The answer must be one of the provided options.')

    class Meta:
        permissions = [
            ('can_add_question', 'Can add question'),
        ]
