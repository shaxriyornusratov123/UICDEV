from django.urls import path

from .views import healthcheck

app_name = "courses"

urlpatterns = [
    path("health/", healthcheck, name="health"),
]
