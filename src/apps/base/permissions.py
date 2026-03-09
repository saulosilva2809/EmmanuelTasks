from rest_framework import permissions

from apps.team.models import TeamMemberModel


class IsManagerOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        project_owner = getattr(obj, 'project', obj).owner 
        if project_owner == request.user:
            return True

        team = getattr(obj, 'team', None)
        if team:
            return TeamMemberModel.objects.filter(
                team=team,
                user=request.user,
                role=TeamMemberModel.RoleChoices.MANAGER
            ).exists()

        return False
