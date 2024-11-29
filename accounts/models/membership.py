from django.db import models
from djangoba_tools.models import Model, PermissionMixinBuilder


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(account__in=user.get_accounts_with_permission(permission))


class Membership(
    PermissionMixinBuilder(filter_func=filter_permission),
    Model,
):
    account = models.ForeignKey(
        "Account", on_delete=models.CASCADE, related_name="memberships"
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="memberships"
    )
    role = models.ForeignKey(
        "Role", on_delete=models.CASCADE, related_name="memberships"
    )

    def __str__(self):
        return f"{self.id}"
