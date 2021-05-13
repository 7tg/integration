from django.contrib import admin

from core.models import Organization
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

