from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView

from .schemas_views import SpectacularV1APIView


urlpatterns = [
    path('admin/', admin.site.urls),

    # api
    path('api/v1/', include('urls.api_v1_urls')),

    # doc
    path('api/v1/schema/', SpectacularV1APIView.as_view(urlconf='urls.api_v1_urls'), name='schema-v1'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema-v1'),),
]
