from django.contrib import admin
from .models import Question
# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'subject', 'question_text', 'answer')
    list_filter = ('class_name', 'subject')
    search_fields = ('question_text', 'subject')
