from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class TaskModel(BaseModel, SoftDeleteModel):
    class PriorityChoices(models.TextChoices):
        LOW = 'LOW', 'Baixa'
        MEDIUM = 'MEDIUM', 'Média'
        HIGH = 'HIGH', 'Alta'
        URGENT = 'URGENT', 'Urgente'

    class StatusChoices(models.TextChoices):
        BACKLOG = 'BACKLOG', 'Backlog'
        TODO = 'TODO', 'A Fazer'
        IN_PROGRESS = 'IN_PROGRESS', 'Em Andamento'
        TESTING = 'TESTING', 'Em Teste'
        DONE = 'DONE', 'Concluído'

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.BACKLOG
    )
    project = models.ForeignKey(
        'project.ProjectModel',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    team = models.ForeignKey(
        'team.TeamModel',
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    sprint = models.ForeignKey(
        'sprint.SprintModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    responsible = models.ForeignKey(
        'authentication.UserModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.MEDIUM
    )
    due_date = models.DateField(null=True, blank=True) # vencimento

    class Meta:
        ordering = ['priority', '-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'#{self.pk} - {self.title}'
