from django.shortcuts import get_object_or_404
from rest_framework import generics, response, status

from apps.team.api.v1.serializers import (
    CreateTeamMemberSerializer,
    DeleteTeamMemberSerializer,
    ListTeamMemberSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.team.models import TeamModel, TeamMemberModel
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
    serializer_class = DeleteTeamMemberSerializer
    
    def get_queryset(self):
        team = get_object_or_404(TeamModel, id=self.kwargs.get('team_id'))
        return TeamMemberSelector.get_all_by_team(team.id)
    
    def destroy(self, request, *args, **kwargs):
        team = get_object_or_404(TeamModel, id=self.kwargs.get('team_id'))
        self.check_object_permissions(self.request, team)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['team_id'] = team.id
        TeamMemberService.delete_team_member(serializer.validated_data)

        return response.Response(status=status.HTTP_204_NO_CONTENT)
