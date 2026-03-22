from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.sprint.api.v1.views import (
    AddTeamInSprintView,
    ListCreateSprintView,
    RetrieveUpdateDestroySprintView,
    RemoveTeamFromSprintView
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
        summary='Excluir uma sprint específico',
        description='Exclui uma sprint específico (soft delete)'
    ),
)(RetrieveUpdateDestroySprintView)


AddTeamInSprintView = extend_schema_view(
    post=extend_schema(
        tags=['Sprint'],
        summary='Adicionar um time em uma sprint',
        description='Adiciona um time em uma sprint'
    )
)(AddTeamInSprintView)


RemoveTeamFromSprintView = extend_schema_view(
    delete=extend_schema(
        tags=['Sprint'],
        summary='Remover um time de uma sprint',
        description='Remove um time de uma sprint'
    )
)(RemoveTeamFromSprintView)
