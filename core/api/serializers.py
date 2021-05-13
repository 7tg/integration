from rest_framework import serializers

from core.models import Organization
from integration.users.api.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)

    class Meta:
        model = Organization
        fields = ("name", "users")


class OrganizationUserSerializer(serializers.Serializer):
    username = serializers.CharField()

