from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class ProjectModel(BaseModel, SoftDeleteModel):
    class ProjectStatusChoices(models.TextChoices):
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
        choices=ProjectStatusChoices.choices,
        default=ProjectStatusChoices.PLANNING
    )
    start_date = models.DateField()
    term = models.DateField()
    slug = models.SlugField(max_length=255, unique=False, blank=True)
    teams = models.ManyToManyField(
        'team.TeamModel',
        related_name='projects',
        blank=True
    )

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

        # regra para garantir o slug único se o Project não estiver deleteado (SOFT DELETE)
        constraints = [
            models.UniqueConstraint(
                fields=['slug'], 
                condition=models.Q(deleted_at__isnull=True),
                name='unique_slug_active_project'
            )
        ]

    def __str__(self):
        return self.name
