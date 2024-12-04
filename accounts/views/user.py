from djangoba_tools.serializers import ModelSerializer
from djangoba_tools.viewsets import ModelViewSet

from ..models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "roles")


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
