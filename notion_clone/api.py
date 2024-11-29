from rest_framework import routers

from documents.views import DocumentViewset

router = routers.DefaultRouter()

router.register(r"documents", DocumentViewset)
