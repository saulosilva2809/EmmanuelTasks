from rest_framework import generics, status
from rest_framework.response import Response

from apps.project.api.v1.serializers import (
    AddTeamInProjectSerializer,
    CreateProjectSerializer,
    ListProjectSerializer,
    UpdateProjectSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.project.selectors import ProjectSelector
from apps.project.services import ProjectService
from apps.team.selectors import TeamSelector


class ListCreateProjectView(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return ProjectSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateProjectSerializer
        return ListProjectSerializer
    
    def perform_create(self, serializer):
        project_instance = ProjectService.create_project(
            serializer.validated_data,
            self.request.user
        )

        serializer.instance = project_instance


class RetrieveUpdateDestroyProjectView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return ProjectSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return UpdateProjectSerializer
        return ListProjectSerializer
    
    def perform_update(self, serializer):
        ProjectService.update_project(
            serializer.validated_data,
            serializer.instance
        )


class AddTeamInProjectView(generics.CreateAPIView):
    permission_classes = [IsManagerOrOwner]
    serializer_class = AddTeamInProjectSerializer

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        project_id = self.kwargs.get('pk')
        updated_project = ProjectService.add_team_in_project(
            serializer.validated_data,
            project_id
        )

        response_serializer = ListProjectSerializer(updated_project)

        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


class RemoveTeamFromProjectView(generics.DestroyAPIView):
    permission_classes = [IsManagerOrOwner]

    def get_queryset(self):
        return TeamSelector.get_all_by_user(self.request.user)

    def destroy(self, request, *args, **kwargs):
        team_id = self.kwargs.get('team_id')
        project_id = self.kwargs.get('project_id')
        updated_project = ProjectService.remove_team_from_project(
            team_id,
            project_id
        )

        response_serializer = ListProjectSerializer(updated_project)

        return Response(response_serializer.data, status=status.HTTP_200_OK)
