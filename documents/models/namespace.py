from django.db import models
from djangoba_tools.models import Model, PermissionMixinBuilder


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(account__in=user.get_accounts_with_permission(permission))


class Namespace(PermissionMixinBuilder(filter_func=filter_permission), Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    account = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="namespaces"
    )

    def __str__(self):
        return self.name
