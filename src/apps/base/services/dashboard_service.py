from apps.project.selectors import ProjectSelector
from apps.sprint.selectors import SprintSelector
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
    

    def get_team_summary(self):
        teams_the_user_is_manager = self.teams.filter(
            manager=self.request.user
        )

        return {
            'teams_the_user_participates': {
                'count': self.teams.count(),
                'teams': [{
                    'name': team.name
                } for team in self.teams]
            },
            'teams_the_user_is_manager': {
                'count': teams_the_user_is_manager.count(),
                'teams': [{
                    'name': team.name
                } for team in teams_the_user_is_manager]
            }
        }
    
    def get_project_summary(self):
        projects_the_user_is_owner= self.projects.filter(
            owner=self.request.user
        )

        return {
            'projects_the_user_participates': {
                'count': self.projects.count(),
                'projects': [{
                    'name': project.name
                } for project in self.projects]
            },
            'projects_the_user_is_owner': {
                'count': projects_the_user_is_owner.count(),
                'projects': [{
                    'name': project.name
                } for project in projects_the_user_is_owner]
            }
        }
    
    def get_sprint_summary(self):
        return {
            'sprint_by_projects': [{
                project.name: project.sprints.count()
            } for project in self.projects],

            'sprint_by_teams': [{
                team.name: team.sprints.count()
            } for team in self.teams],
        }
    
    def get_task_summary(self):
        return [{
            sprint.name: sprint.tasks.count()
        } for sprint in self.sprints]
    
    def format_dashboard(self):
        return {
            'teams': self.get_team_summary(),
            'projects': self.get_project_summary(),
            'sprints': self.get_sprint_summary(),
            'tasks': self.get_task_summary(),
        }
