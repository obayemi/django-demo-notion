from django.db import models
from django_extensions.db.models import TimeStampedModel
from djangoba_tools.models import Model, PermissionMixinBuilder


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(
        document__account__in=user.get_accounts_with_permission(permission)
    )


class Comment(
    PermissionMixinBuilder(filter_func=filter_permission), TimeStampedModel, Model
):
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="comments"
    )
    document = models.ForeignKey(
        "Document", on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()

    def __str__(self):
        return f"{self.id}"
