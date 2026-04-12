from django.db import transaction
from rest_framework.validators import ValidationError

from apps.task.models import TaskModel


class TaskService:
    @staticmethod
    @transaction.atomic()
    def create_task(validated_data: dict):
        TaskService._validate_task_data(validated_data)

        return TaskModel.objects.create(**validated_data)

    @staticmethod
    def _validate_task_data(data: dict, instance: TaskModel = None):
        project = data.get('project') or (instance.project if instance else None)
        team = data.get('team') or (instance.team if instance else None)
        sprint = data.get('sprint') or (instance.sprint if instance else None)
        responsible = data.get('responsible') or (instance.responsible if instance else None)
        status = data.get('status') or (instance.status if instance else None)

        if project and team:
            if not project.teams.filter(pk=team.pk).exists():
                raise ValidationError('Esta equipe não percente a este projeto.')

        if sprint:
            if project and sprint.project != project:
                raise ValidationError('Esta sprint não percente a este projeto.')

            if team and team not in sprint.teams.all():
                raise ValidationError('Esta sprint não percente a esta equipe.')

            if status == TaskModel.TaskStatusChoices.BACKLOG:
                raise ValidationError('O status BACKLOG só pode ser usado quando a task não estiver associada a uma Sprint.')
            
        if responsible and team:
            if not team.team_members.filter(user__pk=responsible.pk).exists():
                raise ValidationError('Esse usuário não pode ser responsável por essa task pro não pertence ao projeto.')
    
    @staticmethod
    @transaction.atomic()
    def update_task(data: dict, instance: TaskModel):
        TaskService._validate_task_data(data, instance)

        for field, value in data.items():
            setattr(instance, field, value)

        instance.save()
        return instance
