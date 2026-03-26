from django.urls import path

from apps.accounts.views import home

app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
]
