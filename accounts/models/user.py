from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from djangoba_tools.models import PermissionMixinBuilder, QuerySet


def filter_permission(cls, queryset, user, permission):
    return queryset.filter(accounts__in=user.get_accounts_with_permission(permission))


class UserManager(BaseUserManager):
    def get_queryset(self):
        return QuerySet(self.model, using=self._db)


class User(
    PermissionMixinBuilder(filter_func=filter_permission),
    AbstractUser,
):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField(_("email address"), unique=True, db_index=True)

    accounts = models.ManyToManyField(
        "Account", related_name="users", through="Membership"
    )

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_accounts_with_permission(self, permission):
        from accounts.models import Account

        return Account.objects.filter(
            memberships__user=self, memberships__role__permissions__codename=permission
        )
