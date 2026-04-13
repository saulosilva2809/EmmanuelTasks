from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.pagination import PaginationAPI
from apps.base.permissions import IsManagerOrOwner
from apps.sprint.api.v1.serializers import (
    AddRemoveTeamInSprintSerializer,
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
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        instance = SprintService.create_sprint(self.request.user, serializer.validated_data)
        response_serializer = ListSprintSerializer(instance)
            
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)


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


class AddTeamInSprintView(generics.CreateAPIView):
    permission_classes = [IsManagerOrOwner]
    serializer_class = AddRemoveTeamInSprintSerializer

    def get_queryset(self):
        return SprintSelector.get_all_by_user(self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sprint = SprintService.add_team_in_sprint(
            self.get_object(),
            serializer.validated_data,
        )

        response = ListSprintSerializer(sprint)
        return Response(response.data, status=status.HTTP_200_OK)


class RemoveTeamFromSprintView(generics.DestroyAPIView):
    permission_classes = [IsManagerOrOwner]
    serializer_class = AddRemoveTeamInSprintSerializer

    def get_queryset(self):
        return SprintSelector.get_all_by_user(self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        sprint = SprintService.remove_team_from_sprint(
            self.get_object(),
            serializer.validated_data
        )
        response = ListSprintSerializer(sprint)

        return Response(response.data, status=status.HTTP_200_OK)
