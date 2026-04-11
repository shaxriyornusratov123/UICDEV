from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.courses.models import Lesson
from apps.courses.serializers import LessonSerializer


class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.select_related("module", "video").all()
    serializer_class = LessonSerializer
    lookup_field = ["id"]
    permission_classes = [AllowAny]


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.select_related("module", "video").all()
    serializer_class = LessonSerializer
