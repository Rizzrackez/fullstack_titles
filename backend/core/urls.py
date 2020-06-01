from django.urls import path
from rest_framework.routers import DefaultRouter
from core.views import *

router = DefaultRouter()
router.register('titles', TitlesViewSet)

urlpatterns = router.urls
