from django.db.models import QuerySet, Q

from apps.authentication.models import UserModel
from apps.team.models import TeamModel


class TeamSelector:
    @staticmethod
    def get_all_by_user(user: UserModel) -> QuerySet[TeamModel]:
        return TeamModel.objects.filter(
            Q(manager=user) | Q(members=user)
        ).select_related(
            'manager'
        ).prefetch_related(
            'members'
        ).distinct() # distinct é importante aqui para não repetir o time se ele for manager e member ao mesmo tempo
