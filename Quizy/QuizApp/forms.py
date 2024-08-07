from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'class_name',
            'subject',
            'question_text',
            'option1',
            'option2',
            'option3',
            'option4',
            'answer'
        ]
