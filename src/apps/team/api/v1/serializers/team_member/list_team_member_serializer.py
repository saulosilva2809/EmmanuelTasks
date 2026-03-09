from rest_framework import serializers

from apps.base.serializers import (
    UserMinSerializer,
    TeamMinSerializer,
    ProjectMinSerializer,
)
from apps.team.models import TeamMemberModel


class ListTeamMemberSerializer(serializers.ModelSerializer):
    user = UserMinSerializer()
    team = TeamMinSerializer()
    project = ProjectMinSerializer()

    class Meta:
        model = TeamMemberModel
        fields = ['id', 'user', 'team', 'project', 'role']
        read_only_fields = ['id']
