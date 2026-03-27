from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.accounts.apis.serializers import EducationSerializer, AuthorSerializer
from apps.accounts.models import Education, Author


class EducationListCreateAPIView(ListCreateAPIView):
    queryset = Education.objects.all().order_by("-created_at")
    serializer_class = EducationSerializer


class EducationRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.select_related("avatar").all().order_by("-created_at")
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.select_related("avatar").all()
    serializer_class = AuthorSerializer
