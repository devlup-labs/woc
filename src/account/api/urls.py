from rest_framework.routers import DefaultRouter
from account.api.views import StudentProfileViewSet, MentorProfileViewSet, UserViewSet, MentorsListViewSet
from .views import AuthenticationCheckAPIView
from django.urls import path

app_name = 'account'

router = DefaultRouter()
router.register(r'student-profile', StudentProfileViewSet, base_name='student-profile')
router.register(r'mentor-profile', MentorProfileViewSet, base_name='mentor-profile')
router.register(r'all-mentors', MentorsListViewSet, base_name='all-mentors')
router.register(r'user', UserViewSet, base_name='user')

urlpatterns = router.urls + [path('auth-check/', AuthenticationCheckAPIView.as_view(), name='auth-check')]
