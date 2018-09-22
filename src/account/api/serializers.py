from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import StudentProfile, MentorProfile


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class MentorProfileSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = MentorProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
