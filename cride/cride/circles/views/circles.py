from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cride.circles.serializers import CircleModelSerializer

from cride.circles.models import Circle


class CircleViewSet(viewsets.ModelViewSet):

    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """List only public circles"""

        queryset = Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset