from rest_framework import serializers

from apps.sprint.models import SprintModel

from .project_min_serializer import ProjectMinSerializer
from .team_min_serializer import TeamMinSerializer


class SprintMinSerializer(serializers.ModelSerializer):
    project = ProjectMinSerializer(read_only=True)
    team = TeamMinSerializer(read_only=True)
    sprint_status = serializers.SerializerMethodField()

    class Meta:
        model = SprintModel
        fields = ('id', 'name', 'project', 'team', 'sprint_status')

    def get_sprint_status(self, obj):
        return obj.get_status_display()
