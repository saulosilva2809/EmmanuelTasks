from django.db.models import QuerySet, Q

from apps.authentication.models import UserModel
from apps.team.models import TeamModel, TeamMemberModel


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

class TeamMemberSelector:
    @staticmethod
    def get_all_by_team(team_id: int) -> QuerySet[TeamMemberModel]:
        return TeamMemberModel.objects.filter(
            team__id=team_id
        ).select_related(
            'user',
            'team',
            'project',
        ).distinct()
