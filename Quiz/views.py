from datetime import timedelta, datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import AllowAny
from django.db.models import Q, When

from .serializers import *
from .models import *
from Account.permissions import *

class StudentQuizList(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request, format=None, **kwargs):
        quiz = kwargs['quiz']
        results = Results.objects.filter(student=request.user, submitted=True)

        if quiz == 'all':
            quizzes = Quizzes.objects.exclude(id__in=results.values('quiz_id'))
            serializer = QuizSerializer(quizzes, many=True)
            return Response(serializer.data)
        elif quiz == 'taken':
            quizzes = Results.objects.filter(student=request.user, submitted=True)
            serializer = StartQuizSerializer(quizzes, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class StartQuiz(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def post(self, request, format=None, **kwargs):
        quiz = Quizzes.objects.get(slug=kwargs['slug'])

        result = Results.objects.get(Q(quiz__slug=quiz.slug) & Q(student=request.user))

        data = request.data
        score = 0
        for index in range(len(data)):
            for key in data[index]:
                if data[index][key] != '':
                    answer = Answer.objects.get(id=data[index][key])
                    if answer.is_right:
                        score += 1

        result.score = score
        result.submitted = True
        result.save()

        return Response(status=status.HTTP_200_OK)

    def get(self, request, format=None, **kwargs):
        quiz = Quizzes.objects.get(slug=kwargs['slug'])

        try:
            Results.objects.get(Q(quiz__slug=quiz.slug) & Q(student=request.user))
        except Results.DoesNotExist:
            # create result object here
            Results.objects.create(
                quiz=quiz,
                student=request.user,
                date_taken=datetime.now(),
                quiz_end=datetime.now() + timedelta(minutes=quiz.time_limit)
            )

        quiz = Results.objects.get(Q(quiz__slug=quiz.slug) & Q(student=request.user))
        serializer = StartQuizSerializer(quiz, many=False)
        return Response(serializer.data)







'''
@api_view(['GET', ])
@permission_classes((AllowAny, ))
def timer(request):
    events = Event.objects.all()
    serializer = EventSerializer(instance=events, many=True)
    return Response(serializer.data)

class Quiz(ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()

class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__slug=kwargs['slug']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class Question(APIView):

    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__slug=kwargs['slug'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

# Experiment
class CrudList(generics.ListCreateAPIView):
    serializer_class = CrudSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['id', 'title']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        This view should return all the data
        for the currently authenticated user.
        """
        user = self.request.user
        return Crud.objects.filter(user=user)


class CrudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crud.objects.all()
    serializer_class = CrudSerializer
    permission_classes = [IsAuthenticated, IsOwner]
'''

