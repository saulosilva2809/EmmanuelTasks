from django.urls import path

from .views import (
    ListCreateProjectView,
    RetrieveUpdateDestroyProjectView
)

from .docs import schemas


urlpatterns = [
    path('', view=ListCreateProjectView.as_view(), name='list_create_project_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroyProjectView.as_view(), name='retrieve_update_destroy_project_view'),
]
