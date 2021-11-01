from rest_framework import serializers
from .models import *

# Quiz without question and answers
class QuizSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(many=False)

    class Meta:
        model = Quizzes
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id', 'answer_text',
        ]

class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['id', 'title', 'answer']

# Quiz including question and answers
class QuizContentSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quizzes
        fields = ['title', 'slug', 'time_limit', 'question']

class StartQuizSerializer(serializers.ModelSerializer):
    quiz = QuizContentSerializer(many=False, read_only=True)

    class Meta:
        model = Results
        fields = ['submitted', 'score', 'date_taken', 'quiz_end', 'quiz']


'''
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
            'slug',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id', 'answer_text', 'is_right'
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = [
            'title', 'answer'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = Questions
        fields = [
            'quiz', 'title', 'answer'
        ]


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crud
        fields = '__all__'
'''

