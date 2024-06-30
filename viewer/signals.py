from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Status, Location, Controller


@receiver(pre_save, sender=Location)
def update_status(sender, instance, **kwargs):
    status_for_delete = "Deleted"
    if instance.pk:
        previous_status = Location.objects.get(pk=instance.pk).status
        new_status = instance.status
        print(previous_status)
        print(new_status)
        if previous_status.name != status_for_delete and new_status.name == status_for_delete:
            delete_status_object = Status.objects.get(name=status_for_delete)
            instance.controller.update(status=delete_status_object)
            for controller in instance.controller.all():
                controller.sensor.update(status=delete_status_object)

@receiver(pre_save, sender=Controller)
def update_status(sender, instance, **kwargs):
    status_for_delete = "Deleted"
    if instance.pk:
        previous_status = Controller.objects.get(pk=instance.pk).status
        new_status = instance.status
        if previous_status.name != status_for_delete and new_status.name == status_for_delete:
            delete_status_object = Status.objects.get(name=status_for_delete)
            instance.sensor.update(status=delete_status_object)