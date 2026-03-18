from rest_framework import serializers

from apps.base.serializers import TeamMinSerializer
from apps.sprint.models import SprintModel


class UpdateSprintSerializer(serializers.ModelSerializer):
    teams = TeamMinSerializer(read_only=True, many=True)

    class Meta:
        model = SprintModel
        fields = [
            'id',
            'project',
            'teams',
            'name',
            'goal',
            'start_date',
            'end_date',
            'status',
        ]
        read_only_fields = ['id']
