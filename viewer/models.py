from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    is_qualified_user = models.BooleanField('qualified status', default=False)

User = get_user_model()

class Status(models.Model):

    name = models.CharField(max_length=255)
    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="status_add")
    modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="status_modified")

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):
    name = models.CharField(max_length=255, null=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="location")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Controller(models.Model):
    name = models.CharField(max_length=255, null=False)
    ip_address = models.GenericIPAddressField(unique=True)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="controller")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="controller")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Sensor(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.IntegerField(validators=[MinValueValidator(0)], null=False)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, related_name="sensor")
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name="sensor")
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class ControllerData(models.Model):
    controller = models.ForeignKey(Controller, on_delete=models.CASCADE, related_name="data")
    data = models.JSONField(null=False, blank=False)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.added}"

