from django.urls import path

from .docs import schemas


urlpatterns = [
    path('token/', schemas.CustomTokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', schemas.CustomTokenRefreshView.as_view(), name='refresh_token'),

]