from import_export import resources
from import_export.fields import Field

from django.utils.translation import gettext as _
from core.models import Transaction


class TransactionResource(resources.ModelResource):
    status = Field()
    type = Field()
    user = Field()

    def dehydrate_status(self, obj):
        return obj.get_status_display()

    def dehydrate_type(self, obj):
        return obj.get_type_display()

    def dehydrate_user(self, obj):
        return obj.user.username if obj.user else _('USER HAS BEEN DELETED')

    class Meta:
        model = Transaction
        export_order = ('id', 'user', 'amount', 'type', 'status')
