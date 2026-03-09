from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class TeamModel(BaseModel, SoftDeleteModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    manager = models.ForeignKey(
        'authentication.UserModel',
        on_delete=models.PROTECT,
        related_name='managed_teams'
    )

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name
