from rest_framework import serializers

from core.models import Organization, Transaction
from integration.users.api.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ("name", "users")


class OrganizationUserSerializer(serializers.Serializer):
    username = serializers.CharField()


class TransactionSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Transaction
        exclude = ()

    def get_status(self, obj):
        return obj.get_status_display()


class TransactionStatusSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        required=True,
        choices=Transaction.Status
    )

    class Meta:
        model = Transaction
        fields = ("status",)
