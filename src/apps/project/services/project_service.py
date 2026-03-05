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
    def _set_slug(name, exclude_id=None):
        slug = slugify(name)
        unique_slug = slug
        
        queryset = ProjectModel.objects.filter(slug=unique_slug)
        if exclude_id:
            queryset = queryset.exclude(id=exclude_id)

        while queryset.exists():
            unique_slug = f'{slug}-{uuid.uuid4().hex[:4]}'
            queryset = ProjectModel.objects.filter(slug=unique_slug)
            if exclude_id:
                queryset = queryset.exclude(id=exclude_id)

        return unique_slug

    @staticmethod
    def update_project(validated_data: dict, instance: ProjectModel):
        old_name = validated_data.get('name')

        if old_name and old_name != instance.name:
            new_slug = ProjectService._set_slug(validated_data['name'], exclude_id=instance.id)
            instance.slug = new_slug
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance
