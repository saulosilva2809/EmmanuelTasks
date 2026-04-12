import uuid

from django.db.models import Q, QuerySet
from django.shortcuts import get_object_or_404

from apps.authentication.models import UserModel
from apps.project.models import ProjectModel


class ProjectSelector:
    @staticmethod
    def get_all_by_user(user: UserModel) -> QuerySet[ProjectModel]:
        return ProjectModel.objects.filter(
            Q(owner=user) | Q(teams__manager=user) | Q(teams__team_members__user=user)
        ).select_related(
            'owner'
        ).prefetch_related(
            'teams',
            'teams__manager',
            'teams__team_members__user'
        ).distinct()
    
    @staticmethod
    def get_by_id(id: uuid.UUID) -> ProjectModel:
        base_filter = ProjectModel.objects.select_related(
            'owner'
        ).prefetch_related(
            'teams'
        )

        return get_object_or_404(base_filter, id=id)
    
    @staticmethod
    def get_by_slug(slug: str) -> ProjectModel:
        base_filter = ProjectModel.objects.select_related(
            'owner'
        ).prefetch_related(
            'teams'
        )

        return get_object_or_404(base_filter, slug=slug)
