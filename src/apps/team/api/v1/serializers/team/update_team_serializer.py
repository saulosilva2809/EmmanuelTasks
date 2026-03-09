from rest_framework import serializers

from apps.team.models import TeamModel


class UpdateTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamModel
        fields = ('name', 'description')
