from rest_framework import generics

from apps.project.api.v1.serializers import (
    CreateProjectSerializer,
    ListProjectSerializer,
    UpdateProjectSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.project.selectors import ProjectSelector
from apps.project.services import ProjectService


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
