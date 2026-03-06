from django.db.models import QuerySet, Q

from apps.authentication.models import UserModel
from apps.sprint.models import SprintModel


class SprintSelector:
    @staticmethod
    def get_all_by_user(user: UserModel) -> QuerySet[SprintModel]:
        return SprintModel.objects.filter(
            Q(project__owner=user) |
            Q(team__manager=user) |
            Q(team__members=user),
        ).select_related(
            'project',
            'team',
        ).distinct() # remover duplicatas
