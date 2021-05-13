from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from core.api.views import OrganizationViewSet, TransactionViewSet
from integration.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("organizations", OrganizationViewSet)
router.register("transactions", TransactionViewSet)


app_name = "api"
urlpatterns = router.urls
