from celery import shared_task
from django.utils import timezone

from apps.invitation.models import InvitationModel


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30, retry_kwargs={'max_retries': 5})
def set_invitations_as_expired(self):
    InvitationModel.objects.filter(
        status=InvitationModel.StatusChoices.PENDING,
        expiration_date__gte=timezone.now()
    ).update(
        status=InvitationModel.StatusChoices.EXPIRED
    )
