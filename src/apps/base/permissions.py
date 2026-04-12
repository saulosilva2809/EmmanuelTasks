from rest_framework import permissions

from apps.project.models import ProjectModel
from apps.sprint.models import SprintModel
from apps.team.models import TeamModel


class IsManagerOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, ProjectModel):
            is_boos = (
                obj.owner == request.user or 
                obj.teams.filter(manager=request.user).exists()
            )
            if is_boos:
                return True
            
            if request.method in permissions.SAFE_METHODS:
                return obj.teams.filter(team_members__user=request.user).exists()

        elif isinstance(obj, TeamModel):
            # se é manager do time ou owner do projeto
            is_boos = (
                obj.manager == request.user or 
                ProjectModel.objects.filter(teams=obj, owner=request.user).exists()
            )
            if is_boos:
                return True

            # permissões de LIST/GET
            if request.method in permissions.SAFE_METHODS: 
                return obj.team_members.filter(user=request.user).exists()
            
        elif isinstance(obj, SprintModel):
            return obj.project.owner == request.user

        return False
