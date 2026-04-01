from rest_framework.serializers import ModelSerializer

from apps.common.models import Region


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
