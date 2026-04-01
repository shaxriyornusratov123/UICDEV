from django.urls import path

from apps.common.views import (
    CountryListCreateAPIView,
    CountryRetrieveUpdateDestroyAPIView,
    RegionListCreateAPIView,
    RegionRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("countries/", CountryListCreateAPIView.as_view(), name="country-list"),
    path(
        "countries/<int:pk>/",
        CountryRetrieveUpdateDestroyAPIView.as_view(),
        name="country-detail",
    ),
    path("regions/", RegionListCreateAPIView.as_view(), name="region-list"),
    path(
        "regions/<int:pk>/",
        RegionRetrieveUpdateDestroyAPIView.as_view(),
        name="region-detail",
    ),
]
