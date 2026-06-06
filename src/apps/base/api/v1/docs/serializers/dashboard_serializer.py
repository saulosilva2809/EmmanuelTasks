from rest_framework import serializers

from apps.base.api.v1.docs.serializers.childs import (
    ProjectsSerializer,
    SprintsSerializer,
    TeamsSerializer
)


class DashboardSerializer(serializers.Serializer):
    teams = TeamsSerializer()
    projects = ProjectsSerializer()
    sprints = SprintsSerializer()
    statistics = ...
