from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.response import Response

from core.api.serializers import OrganizationSerializer, \
    OrganizationUserSerializer
from core.models import Organization
from core.permissions import IsAdminOrReadOnly
from integration.users.models import User


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAdminOrReadOnly, ]

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
