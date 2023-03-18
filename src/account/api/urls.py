from rest_framework.routers import DefaultRouter
from account.api.views import StudentProfileViewSet, MentorProfileViewSet, UserViewSet, UserDetail, UserProfile, StudentProfile
from .views import AuthenticationCheckAPIView
from django.urls import path
from api.views import MyObtainTokenPairView

app_name = 'account'

router = DefaultRouter()
router.register(r'student-profile', StudentProfileViewSet, basename='student-profile')
router.register(r'mentor-profile', MentorProfileViewSet, basename='mentor-profile')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls + [path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check'),
                             path('auth/login/', MyObtainTokenPairView.as_view(), name='login'),
                             path('auth/user/',UserDetail.as_view(), name='user'),
                             path('auth/user/profile/',UserProfile.as_view(), name='user-profile'),
                             path('auth/student-profile/',StudentProfile.as_view(), name='user-profile'),
                             ]
