from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

from accounts.models import Account, Membership, Role, User

admin.site.unregister(Group)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ("@name",)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "account", "role")
    search_fields = ("@user__email", "@account__name")
    list_filter = ["role__name", "account__name"]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    search_fields = ("@name",)


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
    fields = ["account", "role"]
    autocomplete_fields = ["account"]


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "last_login",
        "is_superuser",
        "is_active",
    )
    search_fields = ("@email", "@accounts__name")
    inlines = (MembershipInline,)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    list_filter = ("accounts__name", "is_active", "is_staff", "is_superuser")
