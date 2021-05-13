from config import celery_app
from django.db.transaction import atomic

from core.models import Transaction


@celery_app.task()
def change_transaction_status(transaction_id, status):
    with atomic():
        Transaction.objects.filter(id=transaction_id).update(
            status=status
        )
