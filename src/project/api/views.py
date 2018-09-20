from rest_framework.viewsets import ModelViewSet
from project.api.serializers import ProjectSerializer, ProposalSerializer
from project.models import Proposal, Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProposalUpload(ModelViewSet):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()
