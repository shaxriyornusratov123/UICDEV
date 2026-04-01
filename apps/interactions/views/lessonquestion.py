from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.interactions.serializers import LessonQuestionSerializer
from apps.interactions.models import LessonQuestion


class LessonQuestionvListCreateAPIView(ListCreateAPIView):
    queryset = LessonQuestion.objects.select_related("lesson", "user").all()
    serializer_class = LessonQuestionSerializer
    lookup_field = ["id"]


class LessonQuestionvRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = LessonQuestion.objects.select_related("lesson", "user").all()
    serializer_class = LessonQuestionSerializer
