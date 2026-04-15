from django.db import transaction
from django.db.models import Q
from rest_framework.validators import ValidationError

from apps.authentication.models import UserModel
from apps.sprint.models import SprintModel
from apps.team.models import TeamModel


class SprintService:
    @staticmethod
    @transaction.atomic()
    def create_sprint(user: UserModel, validated_data: dict) -> SprintModel:
        validated_data['user'] = user
        SprintService._validate_project_and_teams(validated_data)
        SprintService._validate_sprint_data(validated_data)

        teams = validated_data.pop('teams', None)
        validated_data.pop('user')
        sprint = SprintModel.objects.create(**validated_data)

        if teams:
            sprint.teams.set(teams)

        return sprint
    
    @staticmethod
    def _validate_project_and_teams(data: dict, instance: SprintModel = None):
        user = data.get('user')
        project = data.get('project') or (instance.project if instance else None)
        status = data.get('status') or (instance.status if instance else SprintModel.SprintStatusChoices.PLANNING)
        teams_id = data.get('teams') or (list(instance.teams.all()) if instance else None)
        teams = TeamModel.objects.filter(id__in=teams_id)
    
        if project and teams:
            valid_teams = project.teams.filter(pk__in=[team.pk for team in teams])
            if valid_teams.count() != len(teams):
                raise ValidationError('Uma ou mais equipes não percentem a este projeto.')

        if status == SprintModel.SprintStatusChoices.ACTIVE:
            active_qs = SprintModel.objects.filter(
                teams__in=teams, 
                status=SprintModel.SprintStatusChoices.ACTIVE
            )
            # se for update ignoramos a própria sprint na busca
            if instance and active_qs:
                active_qs = active_qs.exclude(pk=instance.pk)
            
            if active_qs.exists():
                teams_names_list = active_qs.values_list('teams__name', flat=True).distinct()
                teams_formatted = ', '.join(teams_names_list)
        
                raise ValidationError(f'Os seguintes times já possuem uma Sprint ativa: {teams_formatted}.')

    @staticmethod
    def _validate_sprint_data(data: dict, instance: SprintModel = None):
        start_date = data.get('start_date') or (instance.start_date if instance else None)
        end_date = data.get('end_date') or (instance.end_date if instance else None)
        project = data.get('project') or (instance.project if instance else None)

        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('A data inicial não pode ser maior que a data final.')
            
            if project:
                if start_date < project.start_date:
                    raise ValidationError('A sprint não pode começar antes do projeto.')
    
                if end_date > project.term:
                    raise ValidationError('A sprint não pode terminar depois do prazo do projeto.')
    
    @staticmethod
    @transaction.atomic()
    def update_sprint(data: dict, instance: SprintModel) -> SprintModel:
        SprintService._validate_sprint_data(data, instance)

        for attr, value in data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
    
    @staticmethod
    @transaction.atomic()
    def add_team_in_sprint(instance: SprintModel, data: dict) -> SprintModel:
        teams_id = data.get('teams')
        teams = TeamModel.objects.filter(
            id__in=teams_id
        )
        
        data['teams'] = teams
        SprintService._validate_project_and_teams(data, instance)

        instance.teams.add(*teams) # * para indicar que é mais de um
        instance.save()

        return instance
    
    @staticmethod
    @transaction.atomic()
    def remove_team_from_sprint(instance: SprintModel, data: dict) -> SprintModel:
        teams_id = data.get('teams')
        SprintService._validate_remove_teams(instance, teams_id)

        if teams_id:
            instance.teams.remove(*teams_id)
            instance.save()

        return instance

    @staticmethod
    def _validate_remove_teams(sprint: SprintModel, teams_id: list):
        count_teams_sprint = sprint.teams.filter(id__in=teams_id).count()

        if count_teams_sprint != len(teams_id):
            raise ValidationError('Um ou mais times informados não pertencem ao projeto')
