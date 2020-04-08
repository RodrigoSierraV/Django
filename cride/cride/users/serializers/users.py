from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from cride.users.models import User

class UserLoginSerializer(serializers.Serializer):
    """
        Handles login request data
    """

    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """Checks credentials"""
        print(data.get('email'))
        user = authenticate(username=data['email'], password=data['password'])
        print(user)
        if not user:
            raise serializers.ValidationError('Invalid Credentials')
        self.context['user'] = user
        return data

    def create(self, data):
        """Generates or retrieves a new token"""

        token, created = Token.objects.get_or_create(user=self.context['user'])

        return self.context['user'], token.key


class UserModelSerializer(serializers.ModelSerializer):

        class Meta:

            model = User
            fields = (
                'username',
                'first_name',
                'last_name',
                'phone_number'
            )