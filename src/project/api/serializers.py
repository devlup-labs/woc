from rest_framework import serializers
from project.models import StudentProposal, Project, MentorManual, StudentManual


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class StudentProposalSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProposal
        fields = '__all__'


class StudentProposalApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProposal
        fields = ('id', 'proposalStatus')

class MentorManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = MentorManual
        fields = '__all__'

class StudentManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentManual
        fields = '__all__'