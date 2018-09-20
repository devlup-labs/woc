from rest_framework.routers import DefaultRouter
from account.api.views import StudentProfileViewSet, MentorProfileViewSet

app_name = 'account'

router = DefaultRouter()
router.register(r'student-profile', StudentProfileViewSet, base_name='student-profile')
router.register(r'mentor-profile', MentorProfileViewSet, base_name='mentor-profile')
router.register(r'student-dashboard',StudentProfileViewSet, base_name='student-dashboard')
router.register(r'mentor-dashboard',MentorProfileViewSet, base_name='mentor-dashboard')
urlpatterns = router.urls
