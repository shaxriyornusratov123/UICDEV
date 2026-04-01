from .author_crud import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView
from .education_crud import (
    EducationListCreateAPIView,
    EducationRetrieveUpdateDestroyAPIView,
)
from .auth import UserProfileAPIView, UserRegisterAPIView, UserRegisterConfirmAPIView
from .user_education import (
    UserEducationListCreateAPIView,
    UserEducationRetrieveUpdateDestroyAPIView,
)
from .user_experiance import (
    UserExperianceListCreateAPIView,
    UserExperianceRetrieveUpdateDestroyAPIView,
)
from .user_certificate import (
    UserCertificateListCreateAPIView,
    UserCertificateRetrieveUpdateDestroyAPIView,
)

__all__ = [
    "AuthorListCreateAPIView",
    "AuthorRetrieveUpdateDestroyAPIView",
    "EducationListCreateAPIView",
    "EducationRetrieveUpdateDestroyAPIView",
    "UserProfileAPIView",
    "UserRegisterAPIView",
    "UserRegisterConfirmAPIView",
    "UserEducationListCreateAPIView",
    "UserEducationRetrieveUpdateDestroyAPIView",
    "UserExperianceListCreateAPIView",
    "UserExperianceRetrieveUpdateDestroyAPIView",
    "UserCertificateListCreateAPIView",
    "UserCertificateRetrieveUpdateDestroyAPIView",
]
