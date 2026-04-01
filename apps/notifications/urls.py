from django.urls import path

from apps.notifications.views import (
    NotificationListCreateAPIView,
    NotificationRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "notifications/",
        NotificationListCreateAPIView.as_view(),
        name="notification-list",
    ),
    path(
        "notifications/<int:pk>/",
        NotificationRetrieveUpdateDestroyAPIView.as_view(),
        name="notification-detail",
    ),
]
