from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class SprintModel(BaseModel, SoftDeleteModel):
    class StatusChoices(models.TextChoices):
        PLANNING = 'PLANNING', 'Planejamento'
        ACTIVE = 'ACTIVE', 'Em Execução'
        COMPLETED = 'COMPLETED', 'Finalizada'
        CANCELLED = 'CANCELLED', 'Cancelada'

    project = models.ForeignKey(
        'project.ProjectModel', 
        on_delete=models.CASCADE,
        related_name='sprints'
    )
    team = models.ForeignKey(
        'team.TeamModel',
        on_delete=models.CASCADE,
        related_name='sprints'
    )
    name = models.CharField(max_length=150)
    goal = models.TextField(null=True, blank=True) # objetivo
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANNING
    )

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'

    def __str__(self):
        return f'{self.team.name} - {self.name} ({self.project.name})'
