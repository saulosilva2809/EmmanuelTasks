from rest_framework import generics, permissions

from apps.team.api.v1.serializers import (
    CreateTeamMemberSerializer,
    ListTeamMemberSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.team.permissions import (
    IsProjectOwner,
    IsTeamMember,
    IsTeamManager,
)
from apps.team.selectors import TeamMemberSelector
from apps.team.services import TeamMemberService


class ListCreateTeamMemberView(generics.ListCreateAPIView):
    pagination_class = PaginationAPI

    def get_queryset(self):
        team_id = self.kwargs.get('team_id')
        return TeamMemberSelector.get_all_by_team(team_id)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTeamMemberSerializer
        return ListTeamMemberSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [(permissions.IsAuthenticated & (IsProjectOwner | IsTeamManager))()]
        
        return [(permissions.IsAuthenticated & (IsProjectOwner | IsTeamManager | IsTeamMember))()]

    def perform_create(self, serializer):
        team_id = self.kwargs.get('team_id')
        serializer.validated_data['team_id'] = team_id
        instance = TeamMemberService.create_team_member(serializer.validated_data)

        serializer.instance = instance
