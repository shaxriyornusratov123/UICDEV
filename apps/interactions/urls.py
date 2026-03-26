from django.urls import path

from .views import healthcheck

app_name = "interactions"

urlpatterns = [
    path("health/", healthcheck, name="health"),
]
