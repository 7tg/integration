from django.contrib import admin
from import_export.admin import ExportActionModelAdmin

from core.models import Organization, Transaction
from core.resources import TransactionResource
from integration.users.models import User


class UserInline(admin.TabularInline):
    model = User
    extra = 0


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(ExportActionModelAdmin):
    resource_class = TransactionResource
    list_display = (
        'id',
        'user',
        'amount',
        'type',
        'status',
    )
    search_fields = ('user',)
    list_filter = ('status', 'type')
