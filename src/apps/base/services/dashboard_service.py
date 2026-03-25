from django.db.models import Count
from django.utils import timezone

from apps.project.selectors import ProjectSelector
from apps.sprint.models import SprintModel
from apps.sprint.selectors import SprintSelector
from apps.task.models import TaskModel
from apps.task.selectors import TaskSelector
from apps.team.selectors import TeamSelector


class DashboardService:
    def __init__(self, request):
        self.request = request
        self.teams = self._get_teams()
        self.projects = self._get_projects()
        self.sprints = self._get_sprints()
        self.tasks = self._get_tasks()
    
    # SELECTORS
    def _get_teams(self):
        return TeamSelector.get_all_by_user(self.request.user)
    
    def _get_projects(self):
        return ProjectSelector.get_all_by_user(self.request.user)
    
    def _get_sprints(self):
        return SprintSelector.get_all_by_user(self.request.user)
    
    def _get_tasks(self):
        return TaskSelector.get_all_by_user(self.request.user)

    def _get_tasks_user(self):
        return self._get_tasks().filter(responsible=self.request.user)
    

    def get_team_summary(self):
        teams_the_user_is_manager = self.teams.filter(
            manager=self.request.user
        )

        return {
            'as_member': {
                'count': self.teams.count(),
                'items': [
                    {'id': team.id, 'name': team.name}
                for team in self.teams]
            },
            'as_manager': {
                'count': teams_the_user_is_manager.count(),
                'items': [
                    {'id': team.id, 'name': team.name}
                for team in teams_the_user_is_manager]
            }
        }
    
    def get_project_summary(self):
        projects_the_user_is_owner= self.projects.filter(
            owner=self.request.user
        )

        return {
            'as_member': {
                'count': self.projects.count(),
                'items': [
                    {'id': project.id, 'name': project.name}
                for project in self.projects]
            },
            'as_owner': {
                'count': projects_the_user_is_owner.count(),
                'items': [
                    {'id': project.id, 'name': project.name}
                for project in projects_the_user_is_owner]
            }
        }
    
    def get_active_sprints(self):
        active_sprints = self.sprints.filter(
            status=SprintModel.SprintStatusChoices.ACTIVE
        )

        return [{
            'id': sprint.id,
            'name': sprint.name,
            'goal': sprint.goal,
            'status': sprint.status,
            'progress': sprint.progress,
            'project': {
                'name': sprint.project.name
            },
            'teams': [{
                'name': team.name
            } for team in sprint.teams.all()],
        } for sprint in active_sprints]

    def get_sprints_per_project(self):
        return [{
                'project_name': project.name,
                'sprint_count': project.sprints.count()
            } for project in self.projects],
    
    def get_sprints_per_team(self):
        return [{
                'team_name': team.name,
                'sprint_count': team.sprints.count()
            } for team in self.teams],

    def get_tasks_per_status(self):
        count_tasks_per_status = (
            self._get_tasks_user()
            .values('status')
            .annotate(count=Count('id'))
            .order_by('status')
        )
        return count_tasks_per_status
    
    def get_tasks_per_priority(self):
        count_tasks_per_priority = (
            self._get_tasks_user()
            .values('priority')
            .annotate(count=Count('id'))
            .order_by('priority')
        )
        return count_tasks_per_priority
    
    def overview_tasks(self):
        today = timezone.now()

        # tasks vencidas
        overdue_tasks = self._get_tasks_user().exclude(
            status=TaskModel.TaskStatusChoices.DONE
        ).filter(
            due_date__lte=today
        ).count()
        
        # tasks que vão vencer hoje
        tasks_due_today = self._get_tasks_user().exclude(
            status=TaskModel.TaskStatusChoices.DONE
        ).filter(
            due_date=today
        ).count()

        last_week = today - timezone.timedelta(days=today.weekday())

        # tasks completas essa semana
        tasks_completed_this_week = self._get_tasks_user().filter(
            completed_at__gte=last_week
        ).count()

        # total de tasks do usuário
        total_tasks_assigned = self._get_tasks_user().count()
    
        # total de tasks concluídas do usuário
        total_completed_tasks = self._get_tasks_user().filter(
            completed_at__isnull=False
        ).count()
    
        # tasks totais pendentes
        pending_tasks_count = self._get_tasks_user().exclude(
            status=TaskModel.TaskStatusChoices.DONE
        ).count()

        # porcentagem global de tasks concluídas
        global_progress_percentage = (
            total_tasks_assigned / total_completed_tasks
        ) * 100 if total_tasks_assigned and total_completed_tasks else None

        return {
            'global_progress_percentage': global_progress_percentage,
            'total_tasks_assigned': total_tasks_assigned,
            'total_completed_tasks': total_completed_tasks,
            'pending_tasks_count': pending_tasks_count,
            'tasks_completed_this_week': tasks_completed_this_week,
            'overdue_tasks': overdue_tasks,
            'tasks_due_today': tasks_due_today,
        }

    def format_dashboard(self):
        return {
            'teams': self.get_team_summary(),
            'projects': self.get_project_summary(),
            'sprints': {
                'active_sprints': self.get_active_sprints(),
                'sprints_per_project': self.get_sprints_per_project(),
                'sprints_per_team': self.get_sprints_per_team(),
            },
            'statistics': {
                'task_per_status': self.get_tasks_per_status(),
                'task_per_priority': self.get_tasks_per_priority(),
                'overview_tasks': self.overview_tasks(),
            }
        }
