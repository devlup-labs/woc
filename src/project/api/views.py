from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from account.api.permissions import IsMentor, IsStudent
from project.api.serializers import ProjectSerializer, StudentProposalSerializer, MentorProposalSerializer
from project.models import StudentProposal, Project, MentorProposal


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

    def list(self, request, *args, **kwargs):
        self.queryset = Project.objects.filter(mentorproposal__is_approved=True)
        return super().list(request, args, kwargs)


class StudentProposalViewSet(ModelViewSet):
    serializer_class = StudentProposalSerializer
    queryset = StudentProposal.objects.all()
    permission_classes = [IsStudent]

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            self.permission_classes = [IsMentor]
        return super().get_permissions()


class MentorProposalViewSet(ModelViewSet):
    serializer_class = MentorProposalSerializer
    queryset = MentorProposal.objects.all()
    permission_classes = [IsMentor]

    def get_queryset(self):
        return MentorProposal.objects.filter(project__mentors__user=self.request.user)
