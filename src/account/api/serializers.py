from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import StudentProfile, MentorProfile, BaseProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class MentorProfileSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = MentorProfile
        fields = '__all__'


class MentorsListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = MentorProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'about_me')


class StudentsListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')
    gender = serializers.SerializerMethodField()
    branch = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()

    def get_gender(self, value):
        return value.get_gender_display()

    def get_branch(self, value):
        return value.get_branch_display()

    def get_year(self, value):
        return value.get_year_display()
    

    class Meta:
        model = StudentProfile
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'gender', 'branch', 'year', 'github')

class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = User
        fields = ('id',)

class StudentDetailSerializer (serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = StudentProfile
        fields = ('id',)
