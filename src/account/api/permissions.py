from rest_framework.permissions import BasePermission
from account.models import MentorProfile


class IsMentor(BasePermission):
    """
    Allows access only to instances of MentorProfile class.
    """

    def has_permission(self, request, view):
        return MentorProfile.objects.filter(user=request.user.id).exists()
