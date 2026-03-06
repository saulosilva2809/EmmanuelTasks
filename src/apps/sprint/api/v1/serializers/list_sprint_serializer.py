from rest_framework import serializers

from apps.base.serializers import (
    ProjectMinSerializer,
    TeamMinSerializer
)
from apps.sprint.models import SprintModel


class ListSprintSerializer(serializers.ModelSerializer):
    project = ProjectMinSerializer(read_only=True)
    team = TeamMinSerializer(read_only=True)

    class Meta:
        model = SprintModel
        fields = [
            'id',
            'name',
            'project',
            'team',
            'goal',
            'start_date',
            'end_date',
            'status',
        ]
