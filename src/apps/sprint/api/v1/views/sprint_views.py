from rest_framework import generics

from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.sprint.api.v1.serializers import (
    CreateSprintSerializer,
    ListSprintSerializer,
    UpdateSprintSerializer
)
from apps.sprint.selectors import SprintSelector
from apps.sprint.services import SprintService


class ListCreateSprintView(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return SprintSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateSprintSerializer
        return ListSprintSerializer
    
    def perform_create(self, serializer):
        instance = SprintService.create_sprint(serializer.validated_data)
        serializer.instance = instance


class RetrieveUpdateDestroySprintView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsManagerOrOwner]
    pagination_class = PaginationAPI

    def get_queryset(self):
        return SprintSelector.get_all_by_user(self.request.user)
    
    def get_serializer_class(self):
        if self.request.method in ['PATCH', 'PUT']:
            return UpdateSprintSerializer
        return ListSprintSerializer
    
    def perform_update(self, serializer):
        SprintService.update_sprint(
            serializer.validated_data,
            serializer.instance
        )
