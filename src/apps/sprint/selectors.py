from django.db.models import QuerySet, Q

from apps.authentication.models import UserModel
from apps.sprint.models import SprintModel


class SprintSelector:
    @staticmethod
    def get_all_by_user(user: UserModel) -> QuerySet[SprintModel]:
        return SprintModel.objects.filter(
            Q(project__owner=user) |
            Q(teams__manager=user) |
            Q(teams__team_members__user=user),
        ).select_related(
            'project',
        ).prefetch_related(
            'teams'
        ).distinct() # remover duplicatas
