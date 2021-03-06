from rest_framework.permissions import BasePermission

from cride.circles.models import Membership

class IsActiveCircleMember(BasePermission):
    """
        Allows acces only to circle members
    """

    def has_permission(self, request, view):

        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True