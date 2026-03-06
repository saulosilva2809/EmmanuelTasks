from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.authentication.api.v1.urls')),
    path('projects/', include('apps.project.api.v1.urls')),
    path('sprints/', include('apps.sprint.api.v1.urls')),
    path('teams/', include('apps.team.api.v1.urls')),
]
