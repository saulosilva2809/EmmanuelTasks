import uuid

from datetime import timedelta
from django.db import models
from django.utils import timezone

from apps.base.models import BaseModel


class InvitationModel(BaseModel):
    class RoleChoices(models.TextChoices):
        OWNER = 'OWNER', 'Dono do Projeto'
        MANAGER = 'MANAGER', 'Gerente de Time'
        MEMBER = 'MEMBER', 'Desenvolvedor'
        GUEST = 'GUEST', 'Convidado'

    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        ACCEPTED = 'ACCEPTED', 'Aceito'
        DECLINED = 'DECLINED', 'Recusado'
        EXPIRED = 'EXPIRED', 'Expirado'
        CANCELED = 'CANCELED', 'Cancelado'

    # quem fez o convite
    made_by = models.ForeignKey(
        'authentication.UserModel',
        related_name='invitations_made',
        on_delete=models.CASCADE
    )
    # quem recebeu o convite
    made_for = models.ForeignKey(
        'authentication.UserModel',
        related_name='received_invitations',
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        'project.ProjectModel',
        on_delete=models.CASCADE
    )
    team = models.ForeignKey(
        'team.TeamModel',
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=20, 
        choices=RoleChoices.choices, 
        default=RoleChoices.MEMBER
    )
    link = models.CharField(
        null=True,
        blank=True,
        editable=False,
        unique=True
    )
    expiration_date = models.DateField(
        default=(timezone.now() + timedelta(days=1)),
        editable=False
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices, 
        default=StatusChoices.PENDING
    )

    class Meta:
        verbose_name = 'Invitation'
        verbose_name_plural = 'Invitations'

    def __str__(self):
        return f'Convite de: {self.made_by} para {self.made_for}'

    def _generate_link(self):
        return uuid.uuid4()
    
    def save(self, *args, **kwargs):
        if not self.link:
            self.link = self._generate_link()

        return super().save(*args, **kwargs)
