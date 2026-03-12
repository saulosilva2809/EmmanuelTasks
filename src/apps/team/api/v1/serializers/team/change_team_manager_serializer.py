from rest_framework import serializers


class ChangeTeamManagerSerializer(serializers.Serializer):
    new_manager_id = serializers.UUIDField()
