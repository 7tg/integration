import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from integration.users.models import User


class Organization(models.Model):
    name = models.CharField(_("Name of The Organization"), max_length=50)
    users = models.ManyToManyField(User)


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
    )

    amount = models.DecimalField(
        _("amount"),
        decimal_places=2,
        max_digits=12,
        default=0
    )

    class Status(models.TextChoices):
        INITIATED = 'INI', _('INITIATED')
        PENDING = 'PEN', _('PENDING')
        COMPLETED = 'CMP', _('COMPLETED')
        FAILED = 'FAL', _('FAILED')
        ERROR = 'ERR', _('ERROR')

    status = models.CharField(
        _("status"),
        max_length=3,
        choices=Status.choices,
        default=Status.INITIATED,
        blank=True
    )

    class Type(models.TextChoices):
        IN = 'IN', _('IN')
        OUT = 'OUT', _('OUT')

    type = models.CharField(
        _("type"),
        max_length=3,
        choices=Type.choices,
    )

