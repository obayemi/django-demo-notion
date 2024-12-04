from rest_framework import routers

from accounts.views import AccountViewSet, RoleViewSet
from documents.views import DocumentViewset

router = routers.DefaultRouter()

router.register(r"documents", DocumentViewset)
router.register(r"roles", RoleViewSet)
router.register(r"accounts", AccountViewSet)
