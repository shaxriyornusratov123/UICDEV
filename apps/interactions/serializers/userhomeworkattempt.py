from rest_framework.serializers import ModelSerializer

from apps.interactions.models import UserHomeworkAttempt

class UserHomeworkAttemptSerializer(ModelSerializer):
    class Meta:
        model=UserHomeworkAttempt
        fields=["id","lesson","user","work_file","title","description","created_at","updated_at"]
        read_only_fields=["id","created_at","updated_at"]