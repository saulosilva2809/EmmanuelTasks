from rest_framework import serializers


class AddTeamInSprintSerializer(serializers.Serializer):
    teams = serializers.ListField()
