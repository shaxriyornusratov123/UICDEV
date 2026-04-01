from rest_framework.serializers import ModelSerializer

from apps.accounts.models import UserCertificate


class UserCertificateSerializer(ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = [
            "id",
            "user",
            "course",
            "name",
            "attachment",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "user",
            "course",
            "attachment",
            "created_at",
            "updated_at",
        ]
