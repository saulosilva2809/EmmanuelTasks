from django.db.models import Q, QuerySet

from apps.authentication.models import UserModel
from apps.project.models import ProjectModel


class ProjectSelector:
    @staticmethod
    def get_all_by_user(user: UserModel) -> QuerySet[ProjectModel]:
        return ProjectModel.objects.filter(
            Q(owner=user) | Q(teams__manager=user) | Q(teams__members=user)
        ).distinct().select_related(
            'owner'
        ).prefetch_related(
            'teams',
            'teams__manager',
            'teams__members'
        )
