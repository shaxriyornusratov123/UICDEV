from rest_framework.serializers import ModelSerializer

from apps.courses.models import Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            "id",
            "module",
            "video",
            "name",
            "description",
            "current_rating",
            "type",
            "max_attempts_count",
            "attempt_interval",
            "lesson_order",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
