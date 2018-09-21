from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from account.api.permissions import IsMentor
from project.api.serializers import ProjectSerializer, ProposalSerializer
from project.models import Proposal, Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsMentor]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class ProposalViewSet(ModelViewSet):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()
