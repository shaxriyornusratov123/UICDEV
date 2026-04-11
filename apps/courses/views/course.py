from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from apps.courses.serializers import CourseSerializer
from apps.courses.models import Course


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.select_related("author", "banner", "category").all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.select_related("author", "banner", "category").all()
    serializer_class = CourseSerializer
