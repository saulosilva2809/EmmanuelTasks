from rest_framework import serializers

from apps.base.serializers import (
    TeamMinSerializer,
    UserMinSerializer
)
from apps.project.models import ProjectModel


class ListProjectSerializer(serializers.ModelSerializer):
    owner = UserMinSerializer(read_only=True)
    teams = TeamMinSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectModel
        fields = [
            'id',
            'owner',
            'name',
            'description',
            'status',
            'start_date',
            'term',
            'slug',
            'teams'
        ]
