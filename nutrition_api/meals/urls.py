from django.urls import path

from .views import MealViewSet, TargetViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"meals", MealViewSet, basename="meal")
router.register(r"targets", TargetViewSet, basename="target")


urlpatterns = router.urls