from django.core.management.base import BaseCommand

from apps.authentication.models import UserModel
from apps.invitation.models import InvitationModel
from apps.project.models import ProjectModel
from apps.sprint.models import SprintModel
from apps.task.models import TaskModel
from apps.team.models import TeamModel, TeamMemberModel


class Command(BaseCommand):
    help = 'Limpa todos os dados do banco, exceto superusuários'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Iniciando limpeza do banco...'))
        
        try:
            InvitationModel.objects.all().delete()
            ProjectModel.objects.all().delete()
            SprintModel.objects.all().delete()
            TaskModel.objects.all().delete()
            TeamModel.objects.all().delete()
            TeamMemberModel.objects.all().delete()
            
            # Mantém apenas quem manda no sistema
            UserModel.objects.exclude(is_superuser=True).delete()
            
            self.stdout.write(self.style.SUCCESS('✨ Banco de dados limpo com sucesso!'))
        
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro inesperado: {e}'))
