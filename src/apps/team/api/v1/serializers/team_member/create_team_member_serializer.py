from rest_framework import serializers

from apps.team.models import TeamMemberModel


class CreateTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ['id', 'user', 'team', 'project', 'role']
        read_only_fields = ['id', 'team']
