from rest_framework import serializers

from apps.task.models import TaskModel


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
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
        read_only_fields = ['id']
