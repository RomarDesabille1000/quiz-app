from django.urls import path
from .views import *

'''
path('timer/', timer),
path('', Quiz.as_view()),
path('r/<str:slug>/', RandomQuestion.as_view()),
path('q/<str:slug>/', Question.as_view()),
path('crud/', CrudList.as_view()),
path('crud/<int:pk>/', CrudDetail.as_view()),
'''
urlpatterns = [
    path('<str:quiz>/', StudentQuizList.as_view()),
    path('start/<str:slug>/', StartQuiz.as_view()),
]
