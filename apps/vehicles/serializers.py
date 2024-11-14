"""Serializers for Vehicles App."""

from rest_framework_json_api import serializers

from .models import Location, Make, Automobile, MaintenanceRecord


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = "__all__"


class MakeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Make
        fields = "__all__"


class AutomobileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Automobile
        fields = "__all__"


class MaintenanceRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = MaintenanceRecord
        fields = "__all__"
