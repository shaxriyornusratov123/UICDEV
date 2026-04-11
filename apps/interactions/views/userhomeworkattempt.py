from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.interactions.serializers import UserHomeworkAttemptSerializer
from apps.interactions.models import UserHomeworkAttempt


class UserHomeworkAttemptListCreateAPIView(ListCreateAPIView):
    queryset = UserHomeworkAttempt.objects.select_related(
        "lesson", "user", "work_file"
    ).all()
    serializer_class = UserHomeworkAttemptSerializer
    lookup_field = ["id"]


class UserHomeworkAttemptRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserHomeworkAttempt.objects.select_related(
        "lesson", "user", "work_file"
    ).all()
    serializer_class = UserHomeworkAttemptSerializer
