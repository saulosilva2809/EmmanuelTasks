from rest_framework.validators import ValidationError
from uuid import uuid4

from apps.authentication.models import UserModel
from apps.team.models import TeamModel, TeamMemberModel


class TeamService:
    @staticmethod
    def create_team(validated_data: dict, creator: UserModel) -> TeamModel:
        if not validated_data.get('manager'):
            validated_data['manager'] = creator

        team = TeamModel.objects.create(**validated_data)

        return team
    
    @staticmethod
    def change_team_manager(validated_data: dict, team: TeamModel) -> TeamModel:
        new_manager_id = validated_data.get('new_manager_id')
        new_manager = UserModel.objects.get(id=new_manager_id)

        if not TeamMemberModel.objects.filter(
            user=new_manager_id,
            team=team
        ).exists():
            raise ValidationError('O usuário não pode ser manager pois não está na equipe')

        team.manager = new_manager
        team.save()

        return team
