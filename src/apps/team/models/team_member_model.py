from django.db import models

from apps.base.models import BaseModel, SoftDeleteModel


class TeamMemberModel(BaseModel, SoftDeleteModel):
    class RoleChoices(models.TextChoices):
        MANAGER = 'MANAGER', 'Gerente de Time'
        MEMBER = 'MEMBER', 'Desenvolvedor'
        GUEST = 'GUEST', 'Convidado'

    user = models.ForeignKey(
        'authentication.UserModel', 
        on_delete=models.CASCADE,
        related_name='memberships'
    )
    team = models.ForeignKey(
        'team.TeamModel', 
        on_delete=models.CASCADE,
        related_name='team_members'
    )
    project = models.ForeignKey(
        'project.ProjectModel',
        on_delete=models.CASCADE,
        related_name='project_members'
    )
    role = models.CharField(
        max_length=20, 
        choices=RoleChoices.choices, 
        default=RoleChoices.MEMBER
    )

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Team Member'
        verbose_name_plural = 'Teams Members'
        # Garante que um usuário não entre no mesmo time duas vezes
        unique_together = ('user', 'team')

    def __str__(self):
        return f'{self.user.email} - {self.team.name} ({self.role})'
