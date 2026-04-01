from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.serializers import AuthorSerializer
from apps.accounts.models import Author


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.select_related("avatar").all().order_by("-created_at")
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.select_related("avatar").all()
    serializer_class = AuthorSerializer
    lookup_field = "id"
