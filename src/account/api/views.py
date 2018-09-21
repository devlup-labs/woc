from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import mixins
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer, UserSerializer
from account.models import StudentProfile, MentorProfile
from django.contrib.auth.models import User


class StudentProfileViewSet(ModelViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()


class MentorProfileViewSet(ModelViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()


class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
