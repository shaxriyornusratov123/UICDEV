from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.serializers import UserEducationSerializer
from apps.accounts.models import UserEducation


class UserEducationListCreateAPIView(ListCreateAPIView):
    queryset = UserEducation.objects.select_related("User", "Education").all()
    serializer_class = UserEducationSerializer


class UserEducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserEducation.objects.select_related("User", "Education").all()
    serializer_class = UserEducationSerializer
