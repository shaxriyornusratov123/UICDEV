from .category import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView
from .course import CourseListCreateAPIView, CourseRetrieveUpdateDestroyAPIView
from .tag import TagListCreateAPIView, TagRetrieveUpdateDestroyAPIView
from .module import ModuleListCreateAPIView, ModuleRetrieveUpdateDestroyAPIView
from .lesson import LessonListCreateAPIView, LessonRetrieveUpdateDestroyAPIView

__all__ = [
    "CategoryListCreateAPIView",
    "CategoryRetrieveUpdateDestroyAPIView",
    "CourseListCreateAPIView",
    "CourseRetrieveUpdateDestroyAPIView",
    "TagListCreateAPIView",
    "TagRetrieveUpdateDestroyAPIView",
    "ModuleListCreateAPIView",
    "ModuleRetrieveUpdateDestroyAPIView",
    "LessonRetrieveUpdateDestroyAPIView",
    "LessonListCreateAPIView",
]
