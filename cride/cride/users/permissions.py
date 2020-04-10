from rest_framework.permissions import BasePermission


class IsAccountOwner(BasePermission):
    """Allows access only to objects owned by the User"""
    
    def has_object_permission(self, request, view, obj):
        """Checks obj and user are the same"""
        return request.user == obj