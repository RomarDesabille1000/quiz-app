from django.contrib import admin
from .models import *

admin.site.register(Event)

@admin.register(Quizzes)
class QuizAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'time_limit',
        'teacher',
    ]

    list_display = [
        'slug',
        'title',
        'time_limit',
        'teacher',
        'date_created',
    ]

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_right'
    ]

@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz'
    ]
    list_display = [
        'title',
        'quiz',
        'date_updated'
    ]
    inlines = [
        AnswerInlineModel,
    ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]

@admin.register(Crud)
class CrudAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]


@admin.register(Results)
class QuizAdmin(admin.ModelAdmin):
    fields = ['quiz', 'student', 'score', 'submitted', 'date_taken', 'quiz_end']
    list_display = ['quiz', 'student', 'score', 'date_taken']