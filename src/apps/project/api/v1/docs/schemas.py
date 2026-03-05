from drf_spectacular.utils import extend_schema, extend_schema_view

from apps.project.api.v1.views import (
    ListCreateProjectView,
    RetrieveUpdateDestroyProjectView,
)


ListCreateProjectView = extend_schema_view(
    get=extend_schema(
        tags=['Project'],
        summary='Listar projetos',
        description='Retorna os proejtos que o usuário participa'
    ),
    post=extend_schema(
        tags=['Project'],
        summary='Criar um projeto',
        description='Cria um projeto com os dados informados'
    )
)(ListCreateProjectView)


RetrieveUpdateDestroyProjectView = extend_schema_view(
    get=extend_schema(
        tags=['Project'],
        summary='Detalhar um projeto específico',
        description='Mostra detalhes de um projeto específico'
    ),
    patch=extend_schema(
        tags=['Project'],
        summary='Atualizar um projeto específico',
        description='Atualiza um projeto com os dados informados'
    ),
    put=extend_schema(
        tags=['Project'],
        summary='Atualizar um projeto específico',
        description='Atualiza um projeto com os dados informados'
    ),
    delete=extend_schema(
        tags=['Project'],
        summary='Excluir um projeto específico',
        description='Exclui um projeto específico (soft delete)'
    )
)(RetrieveUpdateDestroyProjectView)
