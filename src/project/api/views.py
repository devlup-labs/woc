from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from account.api.permissions import IsApprovedMentor
from project.api.serializers import ProjectSerializer, StudentProposalSerializer, StudentProposalApproveSerializer, MentorManualSerializer, StudentManualSerializer
from project.models import StudentProposal, Project, MentorManual, StudentManual
from django.contrib.auth.models import User
from account.models import MentorProfile



class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsApprovedMentor]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['retrieve', 'list', 'proposals']:
            self.permission_classes = [AllowAny]
        else :
            id = self.request.data['id']
            user = User.objects.filter(id=id).first()
            mentor = MentorProfile.objects.filter(user=user).first()
            if mentor.is_approved == False:
                self.permission_classes = [IsApprovedMentor]
            else:
                self.permission_classes = [AllowAny]    
        return super().get_permissions()

    @action(methods=['get'], detail=True)
    def all_proposals(self, request, pk=None):
        proposals = get_object_or_404(Project, pk=pk).studentproposal_set.all()
        serializer = StudentProposalSerializer(proposals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class StudentProposalViewSet(ModelViewSet):
    serializer_class = StudentProposalSerializer
    queryset = StudentProposal.objects.all()

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = (AllowAny,)
        return super().get_permissions()

    def get_serializer_class(self):
        return StudentProposalApproveSerializer if self.action == 'approve' else super().get_serializer_class()

    @action(methods=['put'], detail=True)
    def approve(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
    
class MentorManualView(APIView):
    serializer_class = MentorManualSerializer
    queryset = MentorManual.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        manual = MentorManual.objects.all()
        serializer = MentorManualSerializer(manual, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StudentManualView(APIView):
    serializer_class = StudentManualSerializer
    queryset = StudentManual.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        manual = StudentManual.objects.all()
        serializer = StudentManualSerializer(manual, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
