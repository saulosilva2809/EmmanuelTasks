from rest_framework import serializers


class AddTeamInProjectSerializer(serializers.Serializer):
    team_id = serializers.UUIDField(required=True)
