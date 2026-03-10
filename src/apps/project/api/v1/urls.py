from django.urls import path

from .views import (
    AddTeamInProjectView,
    ListCreateProjectView,
    RetrieveUpdateDestroyProjectView,
    RemoveTeamFromProjectView
)

from .docs import schemas


urlpatterns = [
    path('', view=ListCreateProjectView.as_view(), name='list_create_project_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroyProjectView.as_view(), name='retrieve_update_destroy_project_view'),
    path('<uuid:pk>/add-team/', view=AddTeamInProjectView.as_view(), name='add_tem_in_project_view'),
    path('<uuid:project_id>/remove-team/<uuid:team_id>/', view=RemoveTeamFromProjectView.as_view(), name='remove_team_from_project_view'),
]
