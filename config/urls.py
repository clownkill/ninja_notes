from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notes.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
    path("", include("notes.urls", namespace="notes")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)