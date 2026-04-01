from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.courses.serializers import ModuleSerializer
from apps.courses.models import Module


class ModuleListCreateAPIView(ListCreateAPIView):
    queryset = Module.objects.select_related("course").all()
    serializer_class = ModuleSerializer
    lookup_field = ["id"]


class ModuleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.select_related("course").all()
    serializer_class = ModuleSerializer
