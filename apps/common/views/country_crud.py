from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
)
from rest_framework.response import Response

from apps.common.serializers import CountrySerializer
from apps.common.models import Country
from apps.common.tasks import import_countries_and_regions


class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ImportDataAPIView(GenericAPIView):
    def post(self, request, *args, **kwargs):
        result = import_countries_and_regions.delay()
        return Response({"message": "import task started", "task_id": result.id})
