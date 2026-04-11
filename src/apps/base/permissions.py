from rest_framework import permissions

from apps.project.models import ProjectModel
from apps.sprint.models import SprintModel
from apps.team.models import TeamModel, TeamMemberModel


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
            ).exists() or obj.team_members.filter(user=request.user):
                return True
            
        elif isinstance(obj, SprintModel):
            return obj.project.owner == request.user

        print('OBJ não é nenhuma instância')
        return False
