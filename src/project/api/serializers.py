from rest_framework import serializers
from project.models import StudentProposal, Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class StudentProposalSerializer(serializers.ModelSerializer):
    is_accepted = serializers.BooleanField(read_only=True)

    class Meta:
        model = StudentProposal
        fields = '__all__'


class StudentProposalApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProposal
        fields = ('id', 'is_accepted')
