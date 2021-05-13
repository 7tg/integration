from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import OrganizationSerializer, \
    OrganizationUserSerializer, TransactionSerializer, \
    TransactionStatusSerializer
from core.models import Organization, Transaction
from core.permissions import IsAdminOrReadOnly
from core.tasks import change_transaction_status
from integration.users.models import User


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filterset_fields = ('name', 'users',)


    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(users__id=self.request.user.id)
        return self.queryset

    @action(detail=True, methods=['post', 'delete'])
    def user(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()

        serializer = OrganizationUserSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        try:
            user = User.objects.get(
                username=serializer.validated_data['username']
            )
            obj = self.get_object()
            if self.request.method == 'POST':
                obj.users.add(user)
            elif self.request.method == 'DELETE':
                obj.users.remove(user)
            return Response(self.get_serializer(obj).data)
        except User.DoesNotExist as e:
            raise ValidationError({"detail": e})


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filterset_fields = ('user', 'amount', 'status', 'type')

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(user__id=self.request.user.id)
        return self.queryset

    @action(detail=True, methods=['post', 'options'])
    def change_status(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise PermissionDenied()

        if self.request.method == 'OPTIONS':
            metadata_class = self.metadata_class()
            return Response(metadata_class.get_serializer_info(
                TransactionStatusSerializer()
            ))

        serializer = TransactionStatusSerializer(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        try:
            transaction = self.get_object()
            change_transaction_status.delay(
                transaction.id,
                serializer.validated_data['status']
            )
            return Response("", status=HTTP_200_OK)
        except Transaction.DoesNotExist as e:
            raise ValidationError({"detail": e})
