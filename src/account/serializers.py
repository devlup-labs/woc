from rest_framework import serializers
from account.models import StudentProfile
from account.models import MentorProfile


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorProfile
        fields = '__all__'
