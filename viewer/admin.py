from django.contrib import admin
from viewer.models import Status, Location, Controller, Sensor, ControllerData

# Register your models here.
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(Controller)
admin.site.register(Sensor)
admin.site.register(ControllerData)