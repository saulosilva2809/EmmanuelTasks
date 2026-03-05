import uuid

from django.utils.text import slugify

from apps.authentication.models import UserModel
from apps.project.models import ProjectModel


class ProjectService:
    @staticmethod
    def create_project(validated_data: dict, creator: UserModel):
        validated_data['owner'] = creator
        validated_data['slug'] = ProjectService._set_slug(validated_data['name'])

        teams = validated_data.pop('teams', [])

        project = ProjectModel.objects.create(**validated_data)

        if teams:
            project.teams.set(teams)

        return project
    
    @staticmethod
    def _set_slug(name):
        slug = slugify(name)
        unique_slug = slug

        while ProjectModel.objects.filter(slug=slug).exists():
            unique_slug = f'{slug}-{uuid.uuid4().hex[:4]}'

        return unique_slug