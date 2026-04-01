from rest_framework.serializers import ModelSerializer

from apps.accounts.models import UserEducation


class UserEducationSerializer(ModelSerializer):
    class Meta:
        model = UserEducation
        fields = [
            "id",
            "user",
            "education",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
        read_only_fileds = ["id", "created_at", "updated_at", "user", "eduation"]
