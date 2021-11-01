from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('details/', CurrentUserView.as_view()),
    path('register/', RegisterUser.as_view()),
]
