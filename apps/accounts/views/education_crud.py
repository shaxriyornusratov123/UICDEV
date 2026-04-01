from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.serializers import EducationSerializer
from apps.accounts.models import Education


class EducationListCreateAPIView(ListCreateAPIView):
    queryset = Education.objects.all().order_by("-created_at")
    serializer_class = EducationSerializer


class EducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    lookup_field = "id"
