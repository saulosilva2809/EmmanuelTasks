from rest_framework import serializers


class AddRemoveTeamInProjectSerializer(serializers.Serializer):
    teams = serializers.ListField(
        child=serializers.UUIDField(),
        required=True,
        allow_empty=False
    )
