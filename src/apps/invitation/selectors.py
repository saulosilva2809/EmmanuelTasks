from django.db.models import Q

from apps.authentication.models import UserModel
from apps.invitation.models import InvitationModel


class InvitationSelector:
    @staticmethod
    def get_by_user(user: UserModel):
        return InvitationModel.objects.filter(
            Q(made_by=user) |
            Q(made_for=user)
        )
