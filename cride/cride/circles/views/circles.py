from rest_framework import viewsets, mixins

from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.circles import IsCircleAdmin

from cride.circles.serializers import CircleModelSerializer

from cride.circles.models import Circle, Membership


class CircleViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = CircleModelSerializer

    def get_queryset(self):
        """List only public circles"""

        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    
    def perform_create(self, serializer):
        """Assigns circle admin"""

        circle = serializer.save()
        user = self.request.user
        profile = user.profile

        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )

    def get_permissions(self):
        """Assign permissions based on actions"""
        permissions = [IsAuthenticated]

        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]