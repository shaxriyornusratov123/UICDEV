from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.common.serializers import RegionSerializer
from apps.common.models import Region


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.all().order_by("name")
    serializer_class = RegionSerializer


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
