from django.db.models import Q

from apps.authentication.models import UserModel
from apps.task.models import TaskModel


class TaskSelector:
    @staticmethod
    def get_all_by_user(user: UserModel):
        return TaskModel.objects.filter(
            Q(project__owner=user) |
            Q(team__manager=user) |
            Q(team__members=user)
        ).select_related(
            'project',
            'team',
            'sprint'
        ).distinct()
