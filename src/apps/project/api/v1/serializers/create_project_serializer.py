from rest_framework import serializers

from apps.project.models import ProjectModel


class CreateProjectSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = ProjectModel
        fields = [
            'owner',
            'name',
            'description',
            'status',
            'start_date',
            'term',
            'slug',
            'teams'
        ]
