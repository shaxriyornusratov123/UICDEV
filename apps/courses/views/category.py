from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.courses.models import Category
from apps.courses.serializers import CategorySerializer


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
