from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # /admin/
    path("admin/", admin.site.urls),
    # /
    path("", include("core.urls", namespace="core")),
]
