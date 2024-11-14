"""Admin for Vehicles App."""

from django.contrib import admin

from .models import Location, Make, Automobile, MaintenanceRecord


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ["name"]
    list_filter = ["state"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ["name"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(Automobile)
class AutomobileAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ["make_id", "model", "year"]
    list_filter = ["model", "year"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):

    list_per_page = 25
    list_display = ["automobile"]
    list_filter = ["completed"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]
