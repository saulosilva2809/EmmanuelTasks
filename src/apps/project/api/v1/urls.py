from django.urls import path

from .views import (
    ListCreateProjectView,
)


urlpatterns = [
    path('', view=ListCreateProjectView.as_view(), name='list_create_project_view'),
    # path('<uuid:pk>/', view=RetrieveUpdateDestroyTeamView.as_view(), name='retrieve_update_destroy_team_view'),
]
