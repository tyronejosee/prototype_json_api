"""Views for Vehicles App."""

from rest_framework_json_api.views import ModelViewSet

from .models import Location, Make, Automobile, MaintenanceRecord
from .serializers import (
    LocationSerializer,
    MakeSerializer,
    AutomobileSerializer,
    MaintenanceRecordSerializer,
)


class LocationViewSet(ModelViewSet):

    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MakeViewSet(ModelViewSet):

    queryset = Make.objects.all()
    serializer_class = MakeSerializer


class AutomobileViewSet(ModelViewSet):

    queryset = Automobile.objects.all()
    serializer_class = AutomobileSerializer


class MaintenanceRecordViewSet(ModelViewSet):

    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
