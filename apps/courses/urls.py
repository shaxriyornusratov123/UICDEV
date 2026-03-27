from django.urls import path

from apps.courses.apis import (
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    TagListCreateAPIView,
    CourseListCreateAPIView,
)

urlpatterns = [
    path("categories/", CategoryListCreateAPIView.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDestroyAPIView.as_view(),
        name="category-detail",
    ),
    path("tags/", TagListCreateAPIView.as_view(), name="tag-list"),
    path(
        "tags/<int:pk>/",
        TagRetrieveUpdateDestroyAPIView.as_view(),
        name="tag-detail",
    ),
    path("courses/", CourseListCreateAPIView.as_view(), name="course-list"),
    # path(
    #     "courses/<int:pk>/",
    #     CourseRetrieveUpdateDestroyAPIView.as_view(),
    #     name="course-detail",
    # )
]
