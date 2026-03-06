from rest_framework.validators import ValidationError

from apps.sprint.models import SprintModel


class SprintService:
    @staticmethod
    def create_sprint(validated_data: dict) -> SprintModel:
        SprintService._validate_sprint_data(validated_data)

        return SprintModel.objects.create(**validated_data)

    @staticmethod
    def _validate_sprint_data(data: dict, instance: SprintModel = None):
        project = data.get('project') or (instance.project if instance else None)
        team = data.get('team') or (instance.team if instance else None)
        status = data.get('status') or (instance.status if instance else SprintModel.StatusChoices.PLANNING)
        start_date = data.get('start_date') or (instance.start_date if instance else None)
        end_date = data.get('end_date') or (instance.end_date if instance else None)

        if project and team:
            if not project.teams.filter(pk=team.pk).exists():
                raise ValidationError(f'Esta equipe não percente a este projeto.')

        if status == SprintModel.StatusChoices.ACTIVE:
            active_qs = SprintModel.objects.filter(
                team=team, 
                status=SprintModel.StatusChoices.ACTIVE
            )
            # se for update ignoramos a própria sprint na busca
            if instance:
                active_qs = active_qs.exclude(pk=instance.pk)
            
            if active_qs.exists():
                raise ValidationError(f'O time {team.name} já possui uma Sprint ativa.')
    
        if start_date and end_date:
            if start_date > end_date:
                raise ValidationError('A data inicial não pode ser maior que a data final.')
            
            if project:
                if start_date < project.start_date:
                    raise ValidationError('A sprint não pode começar antes do projeto.')
    
                if end_date > project.term:
                    raise ValidationError('A sprint não pode terminar depois do prazo do projeto.')
    
    @staticmethod
    def update_sprint(data: dict, instance: SprintModel) -> SprintModel:
        SprintService._validate_sprint_data(data, instance)

        for attr, value in data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
