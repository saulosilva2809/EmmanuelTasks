from django.db import models

from apps.base.models import BaseModel


class TeamMemberModel(BaseModel):
    class RoleChoices(models.TextChoices):
        OWNER = 'OWNER', 'Dono do Projeto'
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
        related_name='team_members',
        null=True,
        blank=True,
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
    permission_related_project = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'Team Member'
        verbose_name_plural = 'Teams Members'
        # Garante que um usuário não entre no mesmo time duas vezes
        unique_together = ('user', 'team')

    def __str__(self):
        return f'{self.user.email} - {self.team.name if self.team else None} ({self.role})'
    
    def _set_permission_related_project(self):
        if not self.team:
            self.permission_related_project = True
    
    def save(self, *args, **kwargs):
        self._set_permission_related_project()
        return super().save(*args, **kwargs)
