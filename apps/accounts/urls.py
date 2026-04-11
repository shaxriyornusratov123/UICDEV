from django.urls import path

from apps.accounts.views import (
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
    AuthorRetrieveUpdateDestroyAPIView,
    AuthorListCreateAPIView,
    UserCertificateRetrieveUpdateDestroyAPIView,
    UserCertificateListCreateAPIView,
    UserEducationListCreateAPIView,
    UserEducationRetrieveUpdateDestroyAPIView,
    UserExperianceListCreateAPIView,
    UserExperianceRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path("educations/", EducationListCreateAPIView.as_view(), name="education-list"),
    path(
        "educations/<int:pk>/",
        EducationRetrieveUpdateDestroyAPIView.as_view(),
        name="education-detail",
    ),
    path("authors/", AuthorListCreateAPIView.as_view(), name="author-list"),
    path(
        "authors/<int:pk>/",
        AuthorRetrieveUpdateDestroyAPIView.as_view(),
        name="author-detail",
    ),
    path(
        "usercertificate/",
        UserCertificateListCreateAPIView.as_view(),
        name="usercertificate-list",
    ),
    path(
        "usercertificate/<int:pk>/",
        UserCertificateRetrieveUpdateDestroyAPIView.as_view(),
        name="usercertificate-detail",
    ),
    path(
        "usereducation/",
        UserEducationListCreateAPIView.as_view(),
        name="usereducation-list",
    ),
    path(
        "usereducation/<int:pk>/",
        UserEducationRetrieveUpdateDestroyAPIView.as_view(),
        name="usereducation-detail",
    ),
    path(
        "userexperiance/",
        UserExperianceListCreateAPIView.as_view(),
        name="userexperiance-list",
    ),
    path(
        "userexperiance/<int:pk>/",
        UserExperianceRetrieveUpdateDestroyAPIView.as_view(),
        name="userexperiance-detail",
    ),
]
