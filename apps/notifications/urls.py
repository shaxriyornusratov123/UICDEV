from django.urls import path

from .views import healthcheck

app_name = "notifications"

urlpatterns = [
    path("health/", healthcheck, name="health"),
]
