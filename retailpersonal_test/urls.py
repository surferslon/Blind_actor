from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/rest/v1/auto_api/', include('auto_api.urls')),
]
