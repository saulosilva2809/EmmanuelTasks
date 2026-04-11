from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from uuid import UUID, uuid4

from apps.authentication.models import UserModel
from apps.project.models import ProjectModel
from apps.project.selectors import ProjectSelector
from apps.team.models import TeamModel, TeamMemberModel
from apps.team.services import TeamMemberService


class ProjectService:
    @staticmethod
    def create_project(validated_data: dict, creator: UserModel):
        validated_data['owner'] = creator
        validated_data['slug'] = ProjectService._set_slug(validated_data['name'])

        teams = validated_data.pop('teams', [])

        project = ProjectModel.objects.create(**validated_data)
        TeamMemberService.create_owner_project({
            'user': creator,
            'project': project,
            'role': TeamMemberModel.RoleChoices.OWNER,
            'permission_related_project': True
        })

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
            unique_slug = f'{slug}-{uuid4().hex[:4]}'
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
    
    @staticmethod
    def add_team_in_project(validated_data: dict, project_id: UUID):
        teams = []
        ids_list = validated_data.get('teams')
        project = ProjectSelector.get_by_id(project_id)

        for id in ids_list:
            team = get_object_or_404(TeamModel, id=id)

            # para cada time cria uma permissão para o dono do time
            if not project.project_members.filter(
                project=project,
                team=team,
                user=team.manager
            ).exists():
                data = {
                    'user': team.manager,
                    'team': team,
                    'project': project,
                    'role': TeamMemberModel.RoleChoices.MANAGER,
                }
                TeamMemberService.create_team_member(data)
    
            teams.append(team)

        project.teams.set(teams)
        return project

    @staticmethod
    def remove_team_from_project(validated_data: dict, project_id: UUID):
        project = ProjectSelector.get_by_id(project_id)
        team_ids = validated_data.get('teams')

        TeamMemberService.delete_team_members(team_ids, project)
        for uuid in team_ids:
            team = get_object_or_404(TeamModel, id=uuid)
            project.teams.remove(team)

        return project
    
    @staticmethod
    def change_owner_project(validated_data: dict, project_id: UUID):
        new_owner_id = validated_data.get('new_owner')
        new_owner = get_object_or_404(UserModel, id=new_owner_id)
        project = ProjectSelector.get_by_id(project_id)

        # busca e altera TeamMember do antigo dono
        old_project_owner = project.owner

        print('QUERYSET: ', TeamMemberModel.objects.filter(
            user=old_project_owner,
            project=project,
            permission_related_project=True
        ))

        old_permission = TeamMemberModel.objects.get(
            user=old_project_owner,
            project=project,
            permission_related_project=True
        )

        print(f'OLD PERMISSION: {old_permission}')

        old_permission.delete()

        # cria permissão para o novo dono
        TeamMemberService.create_owner_project({
            'user': new_owner,
            'project': project,
            'role': TeamMemberModel.RoleChoices.OWNER,
            'permission_related_project': True
        })

        project.owner = new_owner
        project.save()

        return project
