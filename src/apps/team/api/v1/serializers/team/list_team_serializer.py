from rest_framework import serializers

from apps.team.models import TeamModel
from apps.base.serializers import UserMinSerializer


class ListTeamSerializer(serializers.ModelSerializer):
    manager = UserMinSerializer(read_only=True)

    class Meta:
        model = TeamModel
        fields = ('id', 'name', 'description', 'manager')
