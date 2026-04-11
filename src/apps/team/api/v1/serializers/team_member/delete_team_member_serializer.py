from rest_framework import serializers

from apps.team.models import TeamMemberModel


class DeleteTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMemberModel
        fields = ['id', 'user', 'project']
        read_only_fields = ['id']
