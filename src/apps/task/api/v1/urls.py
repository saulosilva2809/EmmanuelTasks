from django.urls import path

from .views import (
    ListCreateTaskView,
    RetrieveUpdateDestroyTaskView,
    SetTaskCompletedView,
)

from .docs import schemas


urlpatterns = [
    path('', view=ListCreateTaskView.as_view(), name='list_create_task_view'),
    path('<uuid:pk>/', view=RetrieveUpdateDestroyTaskView.as_view(), name='retrieve_update_destroy_task_view'),
    path('set-task-completed/<uuid:pk>/', view=SetTaskCompletedView.as_view(), name='set_task_as_completed_view'),
]
