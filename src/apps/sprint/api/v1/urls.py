from django.urls import path

from .views import (
    AddTeamInSprintView,
    ListCreateSprintView,
    RetrieveUpdateDestroySprintView,
)

from .docs import schemas


urlpatterns = [
    path('', view=ListCreateSprintView.as_view(), name='list_create_sprint_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroySprintView.as_view(), name='retrieve_update_destroy_sprint_view'),

    path('<uuid:pk>/add-team/', view=AddTeamInSprintView.as_view(), name='add_team_in_sprint_view'),
]
