from rest_framework import serializers

from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Circle
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'rides_taken', 'rides_offered',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )