from django.db import transaction
from django.utils import timezone
from rest_framework.validators import ValidationError

from apps.authentication.models import UserModel
from apps.base.tasks.send_email_task import send_email_task
from apps.invitation.models import InvitationModel
from apps.team.models import TeamMemberModel
from apps.team.services import TeamMemberService


class InvitationService:
    @staticmethod
    def email_invitation(data: dict):
        invitation = InvitationService._create_invitation(data)
        InvitationService._send_invitation_by_email(invitation)

        return invitation
    
    @staticmethod
    @transaction.atomic()
    def _create_invitation(data: dict):
        return InvitationModel.objects.create(**data)

    @staticmethod
    def _send_invitation_by_email(invitation: InvitationModel):
        send_email_task.delay(
            subject=f'Convite para o projeto {invitation.project}',
            message=f'http://127.0.0.1:8000/api/v1/invitation/{invitation.link}/',
            recipient_list=[invitation.made_for]
        )

    @staticmethod
    @transaction.atomic()
    def accept_invitation(invitation: InvitationModel, user: UserModel):
        if timezone.now().date() > invitation.expiration_date:
            raise ValidationError('O convite já foi expirado.')

        if invitation.StatusChoices == InvitationModel.StatusChoices.ACCEPTED:
            raise ValidationError('O convite já foi aceito.')

        if invitation.made_for != user.email:
            raise ValidationError('Você não pode aceitar esse convite.')

        user_data = {
            'user': user,
            'team_id': invitation.team.id,
            'project': invitation.project,
            'role': TeamMemberModel.RoleChoices.MEMBER
        }
        TeamMemberService.create_team_member(user_data)
        
        invitation.status = InvitationModel.StatusChoices.ACCEPTED
        invitation.save()

        return invitation
