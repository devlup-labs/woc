from rest_framework.viewsets import ModelViewSet
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer, UserSerializer
from account.models import StudentProfile, MentorProfile
from django.contrib.auth.models import User


class StudentProfileViewSet(ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()


class MentorProfileViewSet(ModelViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
