from rest_framework import serializers

from apps.sprint.models import SprintModel

from .project_min_serializer import ProjectMinSerializer
from .team_min_serializer import TeamMinSerializer


class SprintMinSerializer(serializers.ModelSerializer):
    project = ProjectMinSerializer(read_only=True)
    team = TeamMinSerializer(read_only=True)

    class Meta:
        model = SprintModel
        fields = ('id', 'name', 'project', 'team', 'status')
