from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from account.api.serializers import StudentProfileSerializer, MentorProfileSerializer
from account.api.serializers import UserSerializer, MentorsListSerializer, StudentsListSerializer, UserDetailSerializer, StudentDetailSerializer
from account.models import StudentProfile as StudentDetail , MentorProfile as MentorDetail
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StudentProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                            mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = StudentProfileSerializer
    queryset = StudentDetail.objects.all()

    def get_object(self):
        id = self.request.data['id']
        user = User.objects.filter(id=id).first()
        
        return get_object_or_404(StudentDetail,
                                 user=user) if self.action == 'current' else super().get_object()

    def get_serializer_class(self):
        return StudentsListSerializer if self.action == 'all' else self.serializer_class

    def get_permissions(self):
        self.permission_classes = [AllowAny] if self.action == 'all' else self.permission_classes
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def all(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    @action(methods=['patch'], detail=True)
    def update_profile(self, request, pk=None):
        student_profile = self.get_object()
        serializer = self.get_serializer(student_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
class StudentProfile (APIView):
    serializer_class = StudentDetailSerializer
    queryset = StudentDetail.objects.all()


    def post (self,request, *kwargs,**args):
        print('request_data',request.data)
        id = request.data['user']
        phone = request.data['phone']
        gender = request.data['gender']
        branch = request.data['branch']
        github = request.data['github']
        year = request.data['year']
        print(id)
        user = User.objects.filter(id=id).first()
        if StudentDetail.objects.filter(user=user):
            student.phone = phone
            student.github = github
            student.gender = gender
            student.branch = branch
            student.year = year
            serializer = StudentsListSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        student = StudentDetail.objects.create(user=user,phone=phone,github=github,gender=gender,branch= branch, year=year)
        serializer = StudentsListSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)



class MentorProfileViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = MentorProfileSerializer
    queryset = MentorDetail.objects.all()

    def get_object(self):
        id = self.request.data['id']
        user = User.objects.filter(id=id).first()
        return get_object_or_404(MentorDetail,
                                 user=user) if self.action == 'current' else super().get_object()

    def get_queryset(self, queryset=None):
        return self.queryset.filter(is_approved=True) if self.action == 'all' else super().get_queryset()

    def get_serializer_class(self):
        return MentorsListSerializer if self.action == 'all' else self.serializer_class

    def get_permissions(self):
        self.permission_classes = [AllowAny] if self.action == 'all' else self.permission_classes
        return super().get_permissions()

    @action(methods=['post'], detail=False)
    def current(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)

    @action(methods=['get'], detail=False)
    def all(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    @action(methods=['patch'], detail=True)
    def update_profile(self, request, pk=None):
        mentor_profile = self.get_object()
        serializer = self.get_serializer(mentor_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)

    def get_object(self):
        id = self.kwargs['pk']  # assuming the URL pattern includes the `pk` parameter
        return get_object_or_404(User, id=id)

    @action(methods=['get'], detail=False)
    def current(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def profile(self, request, *args, **kwargs):
        instance = self.get_object()
        mentor_profile = MentorDetail.objects.filter(user=instance)
        student_profile = StudentDetail.objects.filter(user=instance)
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

class UserDetail (APIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def post (self,request, *args, **kwargs):
        id = request.data['id']
        user = User.objects.filter(id=id).first()
        serializer = UserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserProfile (APIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def post (self,request, *args, **kwargs):
        id = request.data['id']
        user = User.objects.filter(id=id).first()
        student_profile = StudentDetail.objects.filter(user=user)
        mentor_profile = MentorDetail.objects.filter(user=user)
        # student_profile = StudentProfile.objects.filter(user=user)
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
        print(request.user)
        authenticated = request.user.is_authenticated
        print(authenticated)
        data = {
            'message': 'Authorized' if authenticated else 'Unauthorized'
        }
        status_code = status.HTTP_200_OK if authenticated else status.HTTP_401_UNAUTHORIZED
        return Response(data, status=status_code)
