from django.contrib.auth.models import User
from rest_framework import serializers

from snippets.models import Snippet


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'snippets', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        return user
