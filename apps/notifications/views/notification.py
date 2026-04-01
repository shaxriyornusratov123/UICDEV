from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.notifications.models import Notification
from apps.notifications.serializers import NotificationSerializer


class NotificationListCreateAPIView(ListCreateAPIView):
    queryset = Notification.objects.select_related(
        "user", "course", "module", "category", "image"
    ).all()
    serializer_class = NotificationSerializer
    lookup_field = ["id"]


class NotificationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.select_related(
        "user", "course", "module", "category", "image"
    ).all()
    serializer_class = NotificationSerializer
