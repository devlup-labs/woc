from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]

if settings.DEBUG:
    from rest_framework.documentation import include_docs_urls
    urlpatterns += [path('api/docs/', include_docs_urls(title='WoC API', public=False))]
