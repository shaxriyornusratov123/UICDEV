from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.interactions.serializers import EnrollmentSerializers
from apps.interactions.models import Enrollment


class EnrollmentListCreateAPIView(ListCreateAPIView):
    queryset = Enrollment.objects.select_related("user", "course").all()
    serializer_class = EnrollmentSerializers
    lookup_field = ["id"]


class EnrollmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.select_related("user", "course").all()
    serializer_class = EnrollmentSerializers
