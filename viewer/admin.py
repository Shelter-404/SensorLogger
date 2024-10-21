from django.contrib import admin
from viewer.models import Status, Location, Controller, Sensor, ControllerData, User




# Register your models here.
admin.site.register(User)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(Controller)
admin.site.register(Sensor)
admin.site.register(ControllerData)