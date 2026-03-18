from rest_framework import serializers

from apps.base.serializers import (
    TeamMinSerializer,
    UserMinSerializer
)
from apps.project.models import ProjectModel


class UpdateProjectSerializer(serializers.ModelSerializer):
    owner = UserMinSerializer(read_only=True)
    slug = serializers.SlugField(read_only=True)
    teams = TeamMinSerializer(read_only=True, many=True)

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
        read_only_fields = ['id']

    def validate(self, data):
        start_date = data.get('start_date') or self.instance.start_date
        term = data.get('term') or self.instance.term
        
        if start_date > term:
            raise serializers.ValidationError(
                {'term': 'A data de prazo não pode ser anterior à data de início.'}
            )
        return data
