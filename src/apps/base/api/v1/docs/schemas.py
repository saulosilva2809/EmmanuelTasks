from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

from apps.base.api.v1.docs.serializers import DashboardSerializer
from apps.base.api.v1.views import DashboardView


DashboardView = extend_schema_view(
    get=extend_schema(
        tags=['Dashboard'],
        summary='Dashboard',
        responses={200: DashboardSerializer}
    )
)(DashboardView)
