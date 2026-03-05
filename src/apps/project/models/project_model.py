from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class ProjectModel(BaseModel, SoftDeleteModel):
    class StatusChoices(models.TextChoices):
        PLANNING = 'PLANNING', 'Planejamento'
        ACTIVE = 'ACTIVE', 'Ativo'
        PAUSED = 'PAUSED', 'Pausado'
        COMPLETED = 'COMPLETED', 'Finalizado'
        CANCELLED = 'CANCELLED', 'Cancelado'

    owner = models.ForeignKey(
        'authentication.UserModel',
        on_delete=models.PROTECT,
        related_name='owner_projects'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PLANNING
    )
    start_date = models.DateField()
    term = models.DateField()
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    teams = models.ManyToManyField(
        'team.TeamModel',
        related_name='projects',
        blank=True
    )

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name
