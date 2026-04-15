from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.validators import ValidationError
from uuid import UUID

from apps.project.models import ProjectModel
from apps.team.models import TeamMemberModel, TeamModel


class TeamMemberService:
    @staticmethod
    @transaction.atomic()
    def create_team_member(validated_data: dict) -> TeamMemberModel:
        TeamMemberService._validate_team_member_data(validated_data)

        user = validated_data.get('user')
        team = validated_data.get('team')
        
        member, created = TeamMemberModel.objects.get_or_create(
            user=user,
            team=team,
            defaults=validated_data
        )
        return member

    @staticmethod
    def _validate_team_member_data(data: dict):
        project = data.get('project')
        team_id = data.get('team_id')
        team = get_object_or_404(TeamModel, id=team_id)

        if project and team:
            if not project.teams.filter(pk=team.pk).exists():
                raise ValidationError('Esta equipe não percente a este projeto.')
            
            existing_model = TeamMemberModel.objects.filter(
                project=project,
                team=team,
                user=data['user']
            ).exists()
            if existing_model:
                raise ValidationError('O usuário selecionado já está no time e projeto.')

    def delete_team_member(id: UUID):
        get_object_or_404(TeamMemberModel, id=id).delete() 
    
    # AVISO: essas functions foram criadas para uso externo dessa APP
    @staticmethod
    @transaction.atomic()
    def delete_team_members(team_ids: list, project: ProjectModel):
        for id in team_ids:
            TeamMemberModel.objects.filter(
                team__id=id,
                project=project
            ).delete()

    @staticmethod
    @transaction.atomic()
    def create_owner_project(data: dict):
        return TeamMemberModel.objects.get_or_create(**data)

    @staticmethod
    @transaction.atomic()
    def create_manager_team(data: dict):
        # retira role de data para fazer a busca
        role = data['role']
        data.pop('role')

        permission_already_exists = TeamMemberModel.objects.filter(
            **data
        )

        # adiciona role novamente ao dict
        data['role'] = role

        if not permission_already_exists.exists():
            TeamMemberModel.objects.create(**data)
            return
    
        permission_already_exists.update(**data)
