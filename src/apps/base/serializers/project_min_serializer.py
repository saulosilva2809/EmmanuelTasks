from rest_framework import serializers

from apps.project.models import ProjectModel

from .user_min_serializer import UserMinSerializer


class ProjectMinSerializer(serializers.ModelSerializer):
    owner = UserMinSerializer(read_only=True)

    class Meta:
        model = ProjectModel
        fields = ('name', 'owner', 'status')
