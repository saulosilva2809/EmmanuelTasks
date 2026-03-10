from rest_framework import serializers


class AddRemoveTeamInProjectSerializer(serializers.Serializer):
    team_id = serializers.UUIDField(required=True)
