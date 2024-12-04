from djangoba_tools.serializers import ModelSerializer
from djangoba_tools.viewsets import ModelViewSet

from ..models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "name")


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
