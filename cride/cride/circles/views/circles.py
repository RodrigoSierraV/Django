from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cride.circles.serializers import CircleModelSerializer

from cride.circles.models import Circle, Membership


class CircleViewSet(viewsets.ModelViewSet):

    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)

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
