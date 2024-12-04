from djangoba_tools.serializers import ModelSerializer
from djangoba_tools.viewsets import ReadonlyViewSet
from rest_framework import serializers

from ..models import Role


class RoleSerializer(ModelSerializer):
    permissions = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="codename"
    )

    class Meta:
        model = Role
        fields = (
            "id",
            "permissions",
        )


class RoleViewSet(ReadonlyViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
