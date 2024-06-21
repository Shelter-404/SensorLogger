from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()

# Create your models here.

class Status(models.Model):
    class StatusChoice(models.TextChoices):
        ENABLE = "ON", "Enable"
        DISABLE = "OFF", "Disable"
        DELETED = "DEL", "Deleted"

    name = models.CharField(
        max_length=3,
        choices=StatusChoice.choices,
        default=StatusChoice.ENABLE,
    )
    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="status_add")
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="status_modified")

class Location(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="location")
    description = models.TextField(blank=True, null=True)

class Controller(models.Model):
    name = models.CharField(max_length=255, null=False)
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="controller")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="controller")
    description = models.TextField(blank=True, null=True)

class Sensor(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="sensor")
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name="sensor")
    description = models.TextField(blank=True, null=True)

class ControllerData(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name="data")
    data = models.JSONField(null=False, blank=False)
    added = models.DateTimeField(auto_now_add=True)
