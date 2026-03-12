from rest_framework import generics, status
from rest_framework.response import Response

from apps.team.api.v1.serializers import (
    ChangeTeamManagerSerializer,
    CreateTeamSerializer,
    ListTeamSerializer,
    UpdateTeamSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.team.selectors import TeamSelector
from apps.team.services import TeamService


class ListCreateTeamView(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrOwner]
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
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return UpdateTeamSerializer
        return ListTeamSerializer


class ChangeTeamManagerView(generics.UpdateAPIView):
    lookup_url_kwarg = 'team_id'
    permission_classes = [IsManagerOrOwner]
    serializer_class = ChangeTeamManagerSerializer

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        team_obj = self.get_object()
        updated_team = TeamService.change_team_manager(
            serializer.validated_data,
            team_obj
        )

        response_serializer = ListTeamSerializer(updated_team)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
