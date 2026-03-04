from django.urls import path

from .views import (
    ListCreateTeamView,
    RetrieveUpdateDestroyTeamView,
)


urlpatterns = [
    path('', view=ListCreateTeamView.as_view(), name='list_create_team_view'),
    path('<uuid:pk>', view=RetrieveUpdateDestroyTeamView.as_view(), name='retrieve_update_destroy_team_view'),
]
