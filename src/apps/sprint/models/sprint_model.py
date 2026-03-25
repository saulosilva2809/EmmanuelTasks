from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class SprintModel(BaseModel, SoftDeleteModel):
    class SprintStatusChoices(models.TextChoices):
        PLANNING = 'PLANNING', 'Planejamento'
        ACTIVE = 'ACTIVE', 'Em Execução'
        COMPLETED = 'COMPLETED', 'Finalizada'
        CANCELLED = 'CANCELLED', 'Cancelada'

    project = models.ForeignKey(
        'project.ProjectModel', 
        on_delete=models.CASCADE,
        related_name='sprints'
    )
    teams = models.ManyToManyField(
        'team.TeamModel',
        related_name='sprints',
        blank=True
    )
    name = models.CharField(max_length=150)
    goal = models.TextField(null=True, blank=True) # objetivo
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=SprintStatusChoices.choices,
        default=SprintStatusChoices.PLANNING
    )
    progress = models.FloatField(null=True, blank=True, editable=False)

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Sprint'
        verbose_name_plural = 'Sprints'

    def __str__(self):
        return f'{self.name} ({self.project.name})'
    
    def _set_progess(self):
        total_tasks = self.tasks.count()
        tasks_completed = self.tasks.filter(completed_at__isnull=False).count()

        progress = (total_tasks / tasks_completed) * 100
        self.progress = progress

    def save(self, *args, **kwargs):
        self._set_progess()
        return super().save(*args, **kwargs)
