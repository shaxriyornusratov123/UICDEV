from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.serializers import UserExperianceSerializer
from apps.accounts.models import UserExperience


class UserExperianceListCreateAPIView(ListCreateAPIView):
    queryset = UserExperience.objects.select_related("User").all()
    serializer_class = UserExperianceSerializer
    lookup_field = ["id"]


class UserExperianceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserExperience.objects.select_related("User").all()
    serializer_class = UserExperianceSerializer
