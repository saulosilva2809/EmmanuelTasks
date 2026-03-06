from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.sprint.api.v1.views import (
    ListCreateSprintView,
    RetrieveUpdateDestroySprintView
)


ListCreateSprintView = extend_schema_view(
    get=extend_schema(
        tags=['Sprint'],
        summary='Listar sprints',
        description='Retorna todas as sprints que o usuário está presente',
    ),
    post=extend_schema(
        tags=['Sprint'],
        summary='Criar uma sprint',
        description='Cria uma sprint com os dados informados'
    )
)(ListCreateSprintView)


RetrieveUpdateDestroySprintView = extend_schema_view(
    get=extend_schema(
        tags=['Sprint'],
        summary='Detalhar uma sprint específica',
        description='Mostra detalhes de uma sprint específico'
    ),
    patch=extend_schema(
        tags=['Sprint'],
        summary='Atualizar uma sprint específica',
        description='Atualiza uma sprint com os dados informados'
    ),
    put=extend_schema(
        tags=['Sprint'],
        summary='Atualizar uma sprint específica',
        description='Atualiza uma sprint com os dados informados'
    ),
    delete=extend_schema(
        tags=['Sprint'],
        summary='Exclui uma sprint específico',
        description='Exclui uma sprint específico (soft delete)'
    ),
)(RetrieveUpdateDestroySprintView)
