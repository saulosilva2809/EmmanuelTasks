from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.task.api.v1.views import (
    ListCreateTaskView,
    RetrieveUpdateDestroyTaskView
)


ListCreateTaskView = extend_schema_view(
    get=extend_schema(
        tags=['Task'],
        summary='Listar tarefas',
        description='Retorna todas as terefas do time do usuário'
    ),
    post=extend_schema(
        tags=['Task'],
        summary='Criar uma tarefa',
        description='Cria uma tarefa com os dados informados'
    ),
)(ListCreateTaskView)


RetrieveUpdateDestroyTaskView = extend_schema_view(
    get=extend_schema(
        tags=['Task'],
        summary='Detalhar uma tarefa específica',
        description='Mostra detalhes de uma tarefa específica'
    ),
    patch=extend_schema(
        tags=['Task'],
        summary='Atualizar uma tarefa específica',
        description='Atualiza uma tarefa com os dados informados'
    ),
    put=extend_schema(
        tags=['Task'],
        summary='Atualizar uma tarefa específica',
        description='Atualiza uma tarefa com os dados informados'
    ),
    delete=extend_schema(
        tags=['Task'],
        summary='Excluir uma tarefa específica',
        description='Exclui uma tarefa específico (soft delete)'
    ),
)(RetrieveUpdateDestroyTaskView)
