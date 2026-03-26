from django.urls import path

from .views import healthcheck

app_name = "common"

urlpatterns = [
    path("health/", healthcheck, name="health"),
]
