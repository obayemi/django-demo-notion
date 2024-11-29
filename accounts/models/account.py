from django.db import models
from djangoba_tools.models import Model, PermissionMixinBuilder


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(id__in=user.get_accounts_with_permission(permission))


class Account(PermissionMixinBuilder(filter_func=filter_permission), Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name
