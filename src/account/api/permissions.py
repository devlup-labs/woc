from rest_framework.permissions import BasePermission
from account.models import MentorProfile, StudentProfile


class IsMentor(BasePermission):
    """
    Allows access only to instances of MentorProfile class.
    """

    def has_permission(self, request, view):
        return MentorProfile.objects.filter(user=request.user.id).exists()


class IsStudent(BasePermission):
    """
    Allows access only to instances of MentorProfile class.
    """

    def has_permission(self, request, view):
        return StudentProfile.objects.filter(user=request.user.id).exists()
