from django.contrib.auth.models import Permission
from django.db import models
from djangoba_tools.models import Model

from accounts.models.permission import RessourcelessPermissionMixin


class Role(
    RessourcelessPermissionMixin,
    Model,
):
    name = models.CharField(max_length=255, unique=True)
    permissions = models.ManyToManyField(Permission, related_name="roles")

    def __str__(self):
        return self.name
