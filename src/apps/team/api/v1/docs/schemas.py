from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.team.api.v1.serializers import ListTeamSerializer
from apps.team.api.v1.views import (
    ListCreateTeamView,
    RetrieveUpdateDestroyTeamView
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
        description='Exclui um time específico',
    ),
)(RetrieveUpdateDestroyTeamView)
