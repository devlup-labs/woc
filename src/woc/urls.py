from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from .views import VueView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

if settings.DEBUG:
    from rest_framework.permissions import AllowAny
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="WoC API",
            default_version='v1',
            description="Documentation for WoC API",
            contact=openapi.Contact(email="opensourceiitj@gmail.com"),
            license=openapi.License(name="MIT License"),
        ),
        validators=['flex', 'ssv'],
        public=True,
        permission_classes=(AllowAny,),
    )

    urlpatterns += [
        re_path(r'^api/docs/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                name='schema-json'),
        re_path(r'^api/docs/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^api/docs/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

urlpatterns += [
    re_path(r'.*', VueView.as_view(), name='vue-js')    # Catch all URL to send all urls to VueJS
]
