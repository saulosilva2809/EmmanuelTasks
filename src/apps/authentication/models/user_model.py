from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.base.models import BaseModel


class UserModel(BaseModel, AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(unique=True)

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
