from django.urls import path

from .views import (
    ListCreateTaskView,
    RetrieveUpdateDestroyTaskView,
)


urlpatterns = [
    path('', view=ListCreateTaskView.as_view(), name='list_create_task_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroyTaskView.as_view(), name='retrieve_update_destroy_task_view'),
]
