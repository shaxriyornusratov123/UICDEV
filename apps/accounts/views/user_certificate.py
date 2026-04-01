from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.serializers import UserCertificateSerializer
from apps.accounts.models import UserCertificate


class UserCertificateListCreateAPIView(ListCreateAPIView):
    queryset = UserCertificate.objects.select_related(
        "user", "courese", "attachment"
    ).all()
    serializer_class = UserCertificateSerializer
    lookup_field = ["id"]


class UserCertificateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserCertificate.objects.select_related(
        "user", "courese", "attachment"
    ).all()
    serializer_class = UserCertificateSerializer
