from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.base.services import DashboardService


class DashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        dash = DashboardService(request)
        response_data = dash.format_dashboard()

        return Response(response_data)
