from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet, StudentProposalViewSet

app_name = 'project'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'student-proposal', StudentProposalViewSet, basename='student-proposal')
urlpatterns = router.urls
