from rest_framework import serializers


# SERIALIZERS AUXILIARES

class ProjectTeamsSerializer(serializers.Serializer):
    name = serializers.CharField()


class ActiveSprintsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    goal = serializers.CharField()
    status = serializers.CharField()
    progress = serializers.IntegerField()
    project = ProjectTeamsSerializer()
    teams = ProjectTeamsSerializer(many=True)


class SprintsPerProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField()
    sprint_count = serializers.IntegerField()


class SprintsPerTeamSerializer(serializers.Serializer):
    team_name = serializers.CharField()
    sprint_count = serializers.IntegerField()

# SERIALIZER PRINCIPAL 

class SprintsSerializer(serializers.Serializer):
    active_sprints = ActiveSprintsSerializer(many=True)
    sprints_per_project = SprintsPerProjectSerializer(many=True)
    sprints_per_team = SprintsPerTeamSerializer(many=True)
