from django.db import models
from django_extensions.db.models import AutoSlugField, TimeStampedModel
from djangoba_tools.models import Model, PermissionMixinBuilder, QuerySet


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(account__in=user.get_accounts_with_permission(permission))


class Document(
    PermissionMixinBuilder(filter_func=filter_permission),
    TimeStampedModel,
    Model,
):
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="created_documents"
    )
    account = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, related_name="documents"
    )

    namespace = models.ForeignKey(
        "Namespace", on_delete=models.CASCADE, related_name="documents"
    )

    title = models.CharField(max_length=255, db_index=True)
    slug = AutoSlugField(populate_from=("account__name", "title"))

    content = models.TextField()

    def __str__(self):
        return self.title
