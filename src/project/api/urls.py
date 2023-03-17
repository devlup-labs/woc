from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet, StudentProposalViewSet, MentorManualView, StudentManualView
from django.urls import path
app_name = 'project'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'student-proposal', StudentProposalViewSet, basename='student-proposal')
urlpatterns = router.urls + [
    path('mentor-manual/', MentorManualView.as_view(), name='mentor-manual'),
    path('student-manual/', StudentManualView.as_view(), name='student-manual'),
]
