from rest_framework import generics

from apps.team.api.v1.serializers import (
    CreateTeamMemberSerializer,
    ListTeamMemberSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.team.selectors import TeamMemberSelector
from apps.team.services import TeamMemberService


class ListCreateTeamMemberView(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        team_id = self.kwargs.get('team_id')
        return TeamMemberSelector.get_all_by_team(team_id)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTeamMemberSerializer
        return ListTeamMemberSerializer

    def perform_create(self, serializer):
        team_id = self.kwargs.get('team_id')
        serializer.validated_data['team_id'] = team_id
        instance = TeamMemberService.create_team_member(serializer.validated_data)

        serializer.instance = instance


class RemoveTeamMemberView(generics.DestroyAPIView):
    permission_classes = [IsManagerOrOwner]
    lookup_url_kwarg = 'member_id' 
    
    def get_queryset(self):
        team_id = self.kwargs.get('team_id')
        return TeamMemberSelector.get_all_by_team(team_id)
