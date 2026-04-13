from rest_framework import serializers

from apps.sprint.models import SprintModel


class CreateSprintSerializer(serializers.ModelSerializer):
    teams = serializers.ListField(
        child=serializers.UUIDField(),
        required=True,
        allow_empty=False,
    )

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
