"""Routers for Vehicles App."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    LocationViewSet,
    MakeViewSet,
    AutomobileViewSet,
    MaintenanceRecordViewSet,
)

router = DefaultRouter()
router.register(r"locations", LocationViewSet)
router.register(r"makes", MakeViewSet)
router.register(r"automobiles", AutomobileViewSet)
router.register(r"maintenance-records", MaintenanceRecordViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
