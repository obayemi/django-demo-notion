from django.contrib import admin

from .models import Comment, Document, Namespace


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "account", "created_by")
    list_filter = ("account",)
    search_fields = ("@title", "@content", "@created_by__email", "@namespace__name")

    autocomplete_fields = ("created_by", "account", "namespace")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "document", "content")
    search_fields = ("@author__email", "@document__title")
    autocomplete_fields = ("author", "document")
    list_filter = ("document__account__name",)


@admin.register(Namespace)
class NamespaceAdmin(admin.ModelAdmin):
    list_display = ("name", "account")
    search_fields = ("@name", "@account__name")
    list_filter = ("account__name",)
