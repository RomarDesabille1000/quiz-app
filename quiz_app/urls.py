from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView, index
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('', TemplateView.as_view(template_name="index.html")),
    path('api/admin/', admin.site.urls),
    path('api/quiz/', include('Quiz.urls')),
    path('api/user/', include('Account.urls')),
    re_path('.*/', index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

