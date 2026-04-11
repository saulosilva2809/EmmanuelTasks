from django.urls import path

from .views import (
    # Team
    ChangeTeamManagerView,
    ListCreateTeamView,
    RetrieveUpdateDestroyTeamView,

    # Team Member
    ListCreateTeamMemberView,
    RemoveTeamMemberView,
)

from .docs import schemas


urlpatterns = [
    # team
    path('', view=ListCreateTeamView.as_view(), name='list_create_team_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroyTeamView.as_view(), name='retrieve_update_destroy_team_view'),
    path('<uuid:team_id>/change-manager/', view=ChangeTeamManagerView.as_view(), name='change_team_manager_view'),

    # teammember
    path('<uuid:team_id>/members/', view=ListCreateTeamMemberView.as_view(), name='list_create_team_member_view'),
    path('<uuid:team_id>/members/delete/', view=RemoveTeamMemberView.as_view(), name='remove_team_member_view'),
]
