"""Models for Vehicles App."""

from django.db import models

from apps.utils.models import BaseModel
from .choices import StatusChoices


class Location(BaseModel):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Make(BaseModel):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Automobile(BaseModel):

    make_id = models.ForeignKey(
        Make,
        on_delete=models.PROTECT,
        related_name="makes",
    )
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    serial_number = models.CharField(max_length=100, unique=True)
    role = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.AVAILABLE,
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name="automobiles",
    )
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.make_id} {self.model} ({self.year}) - {self.serial_number}"


class MaintenanceRecord(BaseModel):

    automobile = models.ForeignKey(
        Automobile,
        on_delete=models.CASCADE,
        related_name="maintenance_records",
    )
    description = models.TextField()
    date = models.DateField()
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Maintenance on {self.automobile} - {self.date}"
