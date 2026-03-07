from rest_framework import serializers

from apps.base.serializers import (
    ProjectMinSerializer,
    SprintMinSerializer,
    TeamMinSerializer,
    UserMinSerializer,
)
from apps.task.models import TaskModel


class ListTaskSerializer(serializers.ModelSerializer):
    project = ProjectMinSerializer(read_only=True)
    team = TeamMinSerializer(read_only=True)
    sprint = SprintMinSerializer(read_only=True)
    responsible = UserMinSerializer(read_only=True)

    class Meta:
        model = TaskModel
        fields = [
            'id',
            'title',
            'description',
            'status',
            'project',
            'team',
            'sprint',
            'responsible',
            'priority',
            'due_date'
        ]
