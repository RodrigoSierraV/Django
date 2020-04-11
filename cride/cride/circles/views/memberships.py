from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404

from cride.circles.models import Circle
from cride.circles.models import Membership
from cride.circles.serializers import MembershipModelSerializer

from rest_framework.permissions import IsAuthenticated
from cride.circles.permissions.memberships import IsActiveCircleMember

class MembershipViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    serializer_class = MembershipModelSerializer
    def dispatch(self, request, *args, **kwargs):
        """Verify that the circle exits"""

        slug_name = kwargs['slug_name']
        self.circle = get_object_or_404(
            Circle, slug_name=slug_name
        )
        return super(MembershipViewSet, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        """Return circle members"""
        return Membership.objects.filter(
            circle=self.circle,
            is_active=True
        )

    def get_permissions(self):
        """Assigns permissions based on acttion"""
        permissions = [IsAuthenticated, IsActiveCircleMember]
        return [p() for p in permissions]

    def get_object(self):
        """Return circle's member by username"""
        return get_object_or_404(
            Membership,
            user__username= self.kwargs['pk'],
            circle=self.circle,
            is_active=True
        )

    def perform_destroy(self, instance):
        """Disables membership"""
        instance.is_active = False
        instance.save()
    
