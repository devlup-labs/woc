from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer, UserSerializer
from account.models import StudentProfile, MentorProfile
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()


class MentorProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()

    def get_object(self):
        return get_object_or_404(MentorProfile,
                                 user=self.request.user) if self.action == 'current' else super().get_object()

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)


class UserViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)

    @action(methods=['get'], detail=False)
    def profile(self, request, *args, **kwargs):
        mentor_profile = MentorProfile.objects.filter(user=self.request.user)
        student_profile = StudentProfile.objects.filter(user=self.request.user)
        if mentor_profile.exists():
            data = {
                'type': 'mentor-profile',
                'id': mentor_profile.first().id
            }
            return Response(data=data, status=status.HTTP_200_OK)
        if student_profile.exists():
            data = {
                'type': 'student-profile',
                'id': student_profile.first().id
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response('', status=status.HTTP_204_NO_CONTENT)


class AuthenticationCheckAPIView(APIView):
    permission_classes = (AllowAny,)
    """
        get:
        Returns the authentication status code and message for current request.
    """

    def get(self, request, *args, **kwargs):
        authenticated = request.user.is_authenticated
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)
