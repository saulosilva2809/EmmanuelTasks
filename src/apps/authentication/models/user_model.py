from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.base.models import BaseModel


class UserModel(BaseModel, AbstractUser):
    class UserRoleChoices(models.TextChoices):
        OWNER = 'OWNER', 'Owner (Dono do Projeto)'
        TEAM_MANAGER = 'TEAM_MANAGER', 'Team Manager (Gerente)'
        MEMBER = 'MEMBER', 'Member (Desenvolvedor)'
        GUEST = 'GUEST', 'Guest (Stakeholder)'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)
    role = models.CharField(choices=UserRoleChoices.choices, default=UserRoleChoices.MEMBER)

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
