from rest_framework import generics, permissions

from apps.project.api.v1.serializers import (
    CreateProjectSerializer,
    ListProjectSerializer,
)
from apps.base.pagination import PaginationAPI
from apps.project.selectors import ProjectSelector
from apps.project.services import ProjectService


class ListCreateProjectView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
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
