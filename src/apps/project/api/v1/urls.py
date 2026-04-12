from django.urls import path

from .views import (
    AddTeamInProjectView,
    ChangeProjectOwnerView,
    ListCreateProjectView,
    RetrieveUpdateDestroyProjectView,
    RemoveTeamFromProjectView
)

from .docs import schemas


urlpatterns = [
    path('', view=ListCreateProjectView.as_view(), name='list_create_project_view'),
    path('<str:slug>/', view=RetrieveUpdateDestroyProjectView.as_view(), name='retrieve_update_destroy_project_view'),
    path('<str:slug>/add-team/', view=AddTeamInProjectView.as_view(), name='add_tem_in_project_view'),
    path('<str:slug>/remove-team/', view=RemoveTeamFromProjectView.as_view(), name='remove_team_from_project_view'),
    path('<str:slug>/change-owner/', view=ChangeProjectOwnerView.as_view(), name='chage_owner_project_view'),
]
