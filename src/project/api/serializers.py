from rest_framework import serializers
from project.models import StudentProposal, Project, MentorProposal


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class StudentProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProposal
        fields = '__all__'


class MentorProposalSerializer(serializers.ModelSerializer):
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = MentorProposal
        exclude = ('id',)
