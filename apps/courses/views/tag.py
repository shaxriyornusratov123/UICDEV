from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.courses.serializers import TagSerializer
from apps.courses.models import Tag


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all().order_by("name")
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
