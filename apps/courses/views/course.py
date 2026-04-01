from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.courses.serializers import CourseSerializer
from apps.courses.models import Course


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.select_related("author", "banner", "category").all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related("author", "banner", "category").all()
    serializer_class = CourseSerializer
