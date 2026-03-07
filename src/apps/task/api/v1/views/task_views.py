from rest_framework import generics, permissions

from apps.base.pagination import PaginationAPI
from apps.task.api.v1.serializers import (
    CreateUpdateTaskSerializer,
    ListTaskSerializer
)
from apps.task.selectors import TaskSelector
from apps.task.services import TaskService


class ListCreateTaskView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TaskSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUpdateTaskSerializer
        return ListTaskSerializer

    def perform_create(self, serializer):
        instance = TaskService.create_task(serializer.validated_data)
        serializer.instance = instance


class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TaskSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['PATCH', 'PUT']:
            return CreateUpdateTaskSerializer
        return ListTaskSerializer
    
    def perform_update(self, serializer):
        TaskService.update_task(
            serializer.validated_data,
            serializer.instance
        )
