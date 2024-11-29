from django.db.models import Exists
from djangoba_tools.models import Model, PermissionMixinBuilder

# requires at least to have an an account allowing in its role to see the ressource
RessourcelessPermissionMixin = PermissionMixinBuilder(
    filter_func=lambda queryset, user, permission: queryset.filter(
        Exists(user.get_orgroles(permission=permission))
    )
)
