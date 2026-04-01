from django.urls import path

from apps.courses.views import (
    CategoryRetrieveUpdateDestroyAPIView,
    CategoryListCreateAPIView,
    TagRetrieveUpdateDestroyAPIView,
    TagListCreateAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    ModuleListCreateAPIView,
    ModuleRetrieveUpdateDestroyAPIView,
    LessonRetrieveUpdateDestroyAPIView,
    LessonListCreateAPIView,
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
    path("", CourseListCreateAPIView.as_view(), name="course-list"),
    path(
        "<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="course-detail",
    ),
    path("", ModuleListCreateAPIView.as_view(), name="module-list"),
    path(
        "<int:pk>/",
        ModuleRetrieveUpdateDestroyAPIView.as_view(),
        name="module-detail",
    ),
    path("", LessonListCreateAPIView.as_view(), name="lesson-list"),
    path(
        "<int:pk>/",
        LessonRetrieveUpdateDestroyAPIView.as_view(),
        name="lesson-detail",
    ),
]
