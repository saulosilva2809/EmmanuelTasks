from rest_framework import permissions

from apps.project.models import ProjectModel
from apps.team.models import TeamModel, TeamMemberModel


class IsTeamManager(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = view.kwargs.get('team_id')
        if not team_id:
            return False
        
        in_team = TeamMemberModel.objects.filter(
            team__id=team_id,
            user=request.user
        ).exists()

        if in_team:
            return TeamModel.objects.filter(
                id=team_id,
                manager=request.user
            ).exists()


class IsTeamMember(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = view.kwargs.get('team_id')
        if not team_id:
            return False
        
        return TeamMemberModel.objects.filter(
            team__id=team_id,
            user=request.user
        ).exists()


class IsProjectOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        team_id = view.kwargs.get('team_id')
        if not team_id:
            return False

        return ProjectModel.objects.filter(
            owner=request.user,
            teams__id=team_id
        ).exists()
