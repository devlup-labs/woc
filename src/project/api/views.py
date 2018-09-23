from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from account.api.permissions import IsApprovedMentor, IsStudent
from project.api.serializers import ProjectSerializer, StudentProposalSerializer, StudentProposalApproveSerializer
from project.models import StudentProposal, Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsApprovedMentor]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['retrieve', 'list', 'all_students']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()

    @action(methods=['get'], detail=True)
    def all_students(self, request, pk=None):
        proposals = get_object_or_404(Project, pk=pk).studentproposal_set.all()
        serializer = StudentProposalSerializer(proposals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentProposalViewSet(ModelViewSet):
    serializer_class = StudentProposalSerializer
    queryset = StudentProposal.objects.all()
    permission_classes = [IsStudent]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [IsApprovedMentor, IsStudent]
        return super().get_permissions()

    def get_serializer_class(self):
        return StudentProposalApproveSerializer if self.action == 'approve' else super().get_serializer_class()

    @detail_route(methods=['put'])
    def approve(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
