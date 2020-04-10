from rest_framework import serializers

from cride.circles.models import Circle


class CircleModelSerializer(serializers.ModelSerializer):

    members_limit = serializers.IntegerField(
        required=False,
        min_value=5,
        max_value=3200
    )

    is_limited = serializers.BooleanField(default=False)

    class Meta:
        
        model = Circle
        fields = (
            'name', 'slug_name',
            'about', 'picture',
            'rides_taken', 'rides_offered',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )

        read_only_fields = (
        'is_public',
        'verified',
        'rides_offered',
        'rides_taken'
        )

    def validate(self, data):
        """Ensures members_limit and is_limited are present"""
        members_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)

        if  is_limited ^ bool(members_limit):
            raise serializers.ValidationError("If circle is limited a member's limit must be provided")
        return data