from rest_framework.validators import ValidationError

from apps.team.models import TeamMemberModel


class TeamMemberService:
    @staticmethod
    def create_team_member(validated_data: dict) -> TeamMemberModel:
        TeamMemberService._validate_team_member_data(validated_data)

        return TeamMemberModel.objects.create(**validated_data)


    @staticmethod
    def _validate_team_member_data(data: dict, instance: TeamMemberModel = None):
        project = data.get('project') or (instance.project if instance else None)
        team = data.get('team') or (instance.team if instance else None)

        if project and team:
            if not project.teams.filter(pk=team.pk).exists():
                raise ValidationError('Esta equipe não percente a este projeto.')
