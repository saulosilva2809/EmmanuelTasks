from rest_framework import serializers


class AddRemoveTeamInSprintSerializer(serializers.Serializer):
    teams = serializers.ListField()
