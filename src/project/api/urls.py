from rest_framework.routers import DefaultRouter
from project.api.views import ProjectViewSet

app_name = 'project'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, base_name='projects')
urlpatterns = router.urls
