from rest_framework.viewsets import ModelViewSet
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer
from account.models import StudentProfile, MentorProfile


class StudentProfileViewSet(ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()


class MentorProfileViewSet(ModelViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()
