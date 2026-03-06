from rest_framework import serializers

from apps.sprint.models import SprintModel


class CreateUpdateSprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = SprintModel
        fields = [
            'id',
            'project',
            'team',
            'name',
            'goal',
            'start_date',
            'end_date',
            'status',
        ]
        read_only_fields = ['id']
