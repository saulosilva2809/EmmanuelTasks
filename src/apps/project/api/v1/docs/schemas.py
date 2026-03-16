from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)

from apps.project.api.v1.serializers import ListProjectSerializer
from apps.project.api.v1.views import (
    AddTeamInProjectView,
    ChangeProjectOwnerView,
    ListCreateProjectView,
    RetrieveUpdateDestroyProjectView,
    RemoveTeamFromProjectView,
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


AddTeamInProjectView = extend_schema_view(
    post=extend_schema(
        tags=['Project'],
        summary='Adicionar um time no projeto',
        description='Adiciona um time no projeto passado na url',
        parameters=[
            OpenApiParameter(
                name='id',
                type=OpenApiTypes.UUID,
                location=OpenApiParameter.PATH,
                description='ID do projeto'
            )
        ],
        responses= {201: ListProjectSerializer}
    )
)(AddTeamInProjectView)


RemoveTeamFromProjectView = extend_schema_view(
    delete=extend_schema(
        tags=['Project'],
        summary='Remover um time no projeto',
        description='Remove um time no projeto passado na url',
        responses={200: ListProjectSerializer}
    )
)(RemoveTeamFromProjectView)


ChangeProjectOwnerView = extend_schema_view(
    put=extend_schema(
        tags=['Project'],
        summary='Alterar dono',
        description='Altera dono do projeto'
    ),
    patch=extend_schema(
        tags=['Project'],
        summary='Alterar dono',
        description='Altera dono do projeto'
    ),
)(ChangeProjectOwnerView)
