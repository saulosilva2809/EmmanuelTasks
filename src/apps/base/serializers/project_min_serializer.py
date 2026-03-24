from rest_framework import serializers

from apps.project.models import ProjectModel

from .user_min_serializer import UserMinSerializer


class ProjectMinSerializer(serializers.ModelSerializer):
    owner = UserMinSerializer(read_only=True)
    project_status = serializers.SerializerMethodField()

    class Meta:
        model = ProjectModel
        fields = ('id', 'name', 'owner', 'project_status')

    def get_project_status(self, obj):
        return obj.get_status_display()
