from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet, MentorProposalViewSet

app_name = 'project'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='projects')
router.register(r'mentorproposal', MentorProposalViewSet, base_name='mentorproposal')
urlpatterns = router.urls
