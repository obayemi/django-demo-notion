from django_filters import rest_framework as filters
from djangoba_tools.serializers import ModelSerializer
from djangoba_tools.viewsets import ModelViewSet
from rest_framework.decorators import action

from ..models import Document

# TODO: prefetch


class DocumentFilter(filters.FilterSet):
    class Meta:
        model = Document
        fields = {
            "id": ["exact"],
            "title": ["exact", "in", "contains"],
            "created_by": ["exact", "in"],
            "account": ["exact", "in"],
            "namespace": ["exact", "in"],
        }


class DocumentSerializer(ModelSerializer):
    class Meta:
        fields = ("id", "title", "content", "created_by", "account", "namespace")
        model = Document


class FullDocumentSerializer(ModelSerializer):

    class Meta:
        fields = (
            "id",
            "title",
            "content",
            "created_by",
            "account",
            "comments",
        )
        model = Document


class DocumentViewset(ModelViewSet):
    queryset = Document.objects.all()
    search_fields = [
        "@title",
        "@created_by__email",
        "@content",
        "@comments__content",
    ]

    def get_serializer_class(self):
        match self.action:
            case "full":
                return FullDocumentSerializer
            case _:
                return DocumentSerializer

    @action(detail=True, methods=["GET"])
    def full(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
