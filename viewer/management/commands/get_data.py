import requests
from django.core.management.base import BaseCommand, CommandError
from ...models import Controller, ControllerData
class Command(BaseCommand):

    def handle(self, *args, **options):
        for mk in Controller.objects.filter(status__name='Enable'):
            url = f"http://{mk.ip_address}/get_data"
            try:
                response = requests.get(url)
                response.raise_for_status()

                data_json = response.json()

                controller_data = ControllerData.objects.create(
                    controller = mk,
                    data = data_json
                )

            except requests.exceptions.RequestException as e:

                print(f"Error: {e}")