from rest_framework import generics, permissions

from apps.team.api.v1.serializers import (
    CreateTeamSerializer,
    ListTeamSerializer,
    UpdateTeamSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.team.selectors import TeamSelector
from apps.team.services import TeamService


class ListCreateTeamView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateTeamSerializer
        return ListTeamSerializer

    def perform_create(self, serializer):
        team_instance = TeamService.create_team(
            validated_data=serializer.validated_data,
            creator=self.request.user
        )

        serializer.instance = team_instance


class RetrieveUpdateDestroyTeamView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return UpdateTeamSerializer
        return ListTeamSerializer
