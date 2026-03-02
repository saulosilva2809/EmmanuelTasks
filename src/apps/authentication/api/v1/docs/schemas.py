from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.authentication.api.v1.docs.serializers import (
    RegisterRequestResponseSerializer,
)
from apps.authentication.api.v1.views import (
    RegisterView,
)


RegisterView = extend_schema_view(
    post=extend_schema(
        tags=['Authentication'],
        summary='Registrar novo usuário',
        description='Cria novo usuário com base nos dados fornecidos',
        request=RegisterRequestResponseSerializer,
        responses={200: RegisterRequestResponseSerializer}
    )
)(RegisterView)


CustomTokenObtainPairView = extend_schema_view(
    post=extend_schema(
        tags=['Authentication'],
        summary='Realizar login',
        description='Gera um par de tokens (access e refresh) para um usuário autenticado.',
    )
)(TokenObtainPairView)


CustomTokenRefreshView = extend_schema_view(
    post=extend_schema(
        tags=['Authentication'],
        summary='Renovar token de acesso',
        description='Utiliza o refresh token para gerar um novo access token.',
    )
)(TokenRefreshView)
