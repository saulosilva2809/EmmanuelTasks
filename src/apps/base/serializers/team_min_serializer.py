from rest_framework import serializers

from apps.team.models import TeamModel

from .user_min_serializer import UserMinSerializer


class TeamMinSerializer(serializers.ModelSerializer):
    manager = UserMinSerializer(read_only=True)

    class Meta:
        model = TeamModel
        fields = ('name', 'manager')
