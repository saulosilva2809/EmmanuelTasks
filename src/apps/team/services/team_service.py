from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError

from apps.authentication.models import UserModel
from apps.team.models import TeamModel, TeamMemberModel
from apps.team.services import TeamMemberService


class TeamService:
    @staticmethod
    @transaction.atomic()
    def create_team(validated_data: dict, creator: UserModel) -> TeamModel:
        if not validated_data.get('manager'):
            validated_data['manager'] = creator

        team = TeamModel.objects.create(**validated_data)

        return team
    
    @staticmethod
    @transaction.atomic()
    def change_team_manager(validated_data: dict, team: TeamModel) -> TeamModel:
        new_manager_id = validated_data.get('new_manager_id')
        new_manager = get_object_or_404(UserModel, id=new_manager_id)

        if not TeamMemberModel.objects.filter(
            user=new_manager_id,
            team=team
        ).exists():
            raise ValidationError('O usuário não pode ser manager pois não está na equipe')
        
        # busca e deleta antiga permissão
        old_permission = TeamMemberModel.objects.get(
            user=team.manager,
            team=team
        )
        old_permission.delete()

        # cria nova permissão para o novo manager
        TeamMemberService.create_manager_team(data={
            'user': new_manager,
            'team': team,
            'project': old_permission.project,
            'role': TeamMemberModel.RoleChoices.MANAGER
        })

        team.manager = new_manager
        team.save()

        return team
