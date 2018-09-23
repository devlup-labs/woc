from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet, StudentProposalViewSet

app_name = 'project'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'student-proposal', StudentProposalViewSet, base_name='student-proposal')
urlpatterns = router.urls
