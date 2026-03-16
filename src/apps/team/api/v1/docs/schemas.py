from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.team.api.v1.serializers import ListTeamSerializer
from apps.team.api.v1.views import (
    ChangeTeamManagerView,
    ListCreateTeamMemberView,
    ListCreateTeamView,
    RemoveTeamMemberView,
    RetrieveUpdateDestroyTeamView,
)


ListCreateTeamView = extend_schema_view(
    get=extend_schema(
        tags=['Team'],
        summary='Listar times',
        description='Retorna todos os times que o usuário participa',
    ),
    post=extend_schema(
        tags=['Team'],
        summary='Criar um time',
        description='Cria um time com os dados informados',
        responses=ListTeamSerializer
    )
)(ListCreateTeamView)


RetrieveUpdateDestroyTeamView = extend_schema_view(
    get=extend_schema(
        tags=['Team'],
        summary='Detalhar um time específico',
        description='Mostra detalhes de um time específico',
    ),
    patch=extend_schema(
        tags=['Team'],
        summary='Atualizar um time específico',
        description='Atualiza um time com os dados informados',
    ),
    put=extend_schema(
        tags=['Team'],
        summary='Atualizar um time específico',
        description='Atualiza um time com os dados informados',
    ),
    delete=extend_schema(
        tags=['Team'],
        summary='Excluir um time específico',
        description='Exclui um time específico (soft delete)',
    ),
)(RetrieveUpdateDestroyTeamView)


ListCreateTeamMemberView = extend_schema_view(
    get=extend_schema(
        tags=['Team Member'],
        summary='Listar membros',
        description='Lista todos os membros de um time.'
    ),
    post=extend_schema(
        tags=['Team Member'],
        summary='Adicionar um membros',
        description='Adiciona um membro em um time.'
    ),
)(ListCreateTeamMemberView)

RemoveTeamMemberView = extend_schema_view(
    delete=extend_schema(
        tags=['Team Member'],
        summary='Deletar membro',
        description='Deleta um membro de um time.',
        responses={204: None}
    )
)(RemoveTeamMemberView)


ChangeTeamManagerView = extend_schema_view(
    put=extend_schema(
        tags=['Team'],
        summary='Alterar gerente',
        description='Altera gerente da equipe'
    ),
    patch=extend_schema(
        tags=['Team'],
        summary='Alterar gerente',
        description='Altera gerente da equipe'
    ),
)(ChangeTeamManagerView)
