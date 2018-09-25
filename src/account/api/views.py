from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer, UserSerializer
from account.models import StudentProfile, MentorProfile
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentProfileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentProfile.objects.all()


class MentorProfileViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorProfile.objects.all()


class UserViewSet(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)


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
