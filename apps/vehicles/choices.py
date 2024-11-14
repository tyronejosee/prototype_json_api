"""Choices for Vehicles App."""

from django.db import models


class StatusChoices(models.TextChoices):

    AVAILABLE = "available", "Available"
    RENTED = "rented", "Rented"
    MAINTENANCE = "maintenance", "Maintenance"
