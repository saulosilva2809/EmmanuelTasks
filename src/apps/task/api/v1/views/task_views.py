from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.task.api.v1.serializers import (
    CreateUpdateTaskSerializer,
    ListTaskSerializer
)
from apps.task.selectors import TaskSelector
from apps.task.services import TaskService


class ListCreateTaskView(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return TaskSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUpdateTaskSerializer
        return ListTaskSerializer

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        instance = TaskService.create_task(serializer.validated_data)
        serializer.instance = instance


class RetrieveUpdateDestroyTaskView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrOwner]
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


class SetTaskCompletedView(generics.CreateAPIView):
    permission_classes = [IsManagerOrOwner]

    def get_queryset(self):
        return TaskSelector.get_all_by_user(self.request.user)
    
    def create(self, request, *args, **kwargs):
        task_obj = self.get_object()

        task = TaskService.set_task_as_completed(
            task_obj,
            self.request.user
        )
        response = ListTaskSerializer(task)

        return Response(response.data, status=status.HTTP_200_OK)
