from django.urls import path

from apps.base.api.v1.views import DashboardView

from .docs import schemas


urlpatterns = [
    path('dashboard/', view=DashboardView.as_view(), name='dashoard_view')
]
