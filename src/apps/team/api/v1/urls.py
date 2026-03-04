from django.urls import path

from .views import (
    ListCreateTeamView
)


urlpatterns = [
    path('', view=ListCreateTeamView.as_view(), name='list_create_team_view'),
]
