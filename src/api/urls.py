from django.urls import path, include
from .views import LoginAPIView, LogoutAPIView, CsrfTokenAPIView, MyObtainTokenPairView
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'api'

urlpatterns = [
    path('account/', include('account.api.urls')),
    path('project/', include('project.api.urls')),
    path('csrf-token/', CsrfTokenAPIView.as_view(), name='token'),
    path('google-login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/login/', MyObtainTokenPairView.as_view(), name='login'),
    
    ]
