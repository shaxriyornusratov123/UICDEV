from django.urls import path

from apps.accounts.apis import (
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    AuthorListCreateAPIView,
)

urlpatterns = [
    path("educations/",EducationListCreateAPIView.as_view(),name="education-list"),
    path(
        "educations/<int:pk>/",
        EducationRetrieveUpdateDestroyAPIView.as_view(),
        name="education-detail",
    ),
    path("auhtors/",AuthorListCreateAPIView.as_view(),name="auhtor-list"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyAPIView.as_view(),
        name="author-detail",
    ),
]
