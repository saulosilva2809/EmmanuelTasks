from rest_framework import permissions

from apps.project.models import ProjectModel
from apps.team.models import TeamModel


class IsManagerOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, ProjectModel):
            if obj.owner == request.user:
                return True

        elif isinstance(obj, TeamModel):
            if obj.manager == request.user or ProjectModel.objects.filter(
                teams=obj,
                owner=request.user
            ).exists():
                return True

        return False
