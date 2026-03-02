from django.urls import path, include


urlpatterns = [
    path('auth/', include('apps.authentication.api.v1.urls'))
]
