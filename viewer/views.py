from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ControllerCreateForm, SensorForm, LocationForm
from .models import Location, Status, Sensor, Controller, ControllerData
from .decorators import qualification_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home")


# For future features
# class ManageView(LoginRequiredMixin, View):
#     locations = Location.objects.all()
#     controllers = Controller.objects.all()
#     sensors = Sensor.objects.all()
#     def get(self, request, *args, **kwargs):
#         return render(request, template_name="management.html", context={'locations': self.locations, 'controllers': self.controllers, 'sensors': self.sensors})

class LocationView(LoginRequiredMixin, ListView):
    template_name = "locations.html"
    model = Location
    context_object_name = 'locations'

    def get_queryset(self):
        return Location.objects.exclude(status__name='Deleted')

class LocationAddView(LoginRequiredMixin, CreateView):
    model = Location
    form_class = LocationForm
    template_name = "form.html"
    success_url = reverse_lazy("manage")
    # permission_required = "viewer.add_location"



class ControllerAddView(LoginRequiredMixin, CreateView):
    model = Controller
    form_class = ControllerCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("manage")
    # permission_required = "viewer.add_controller"

    # def form_valid(self, form):
    #     # Create a new Status object
    #     status = Status.objects.create(
    #         added_by=self.request.user,
    #         modified_by=self.request.user
    #     )
    #     # Assign the created status to the location
    #     form.instance.status = status
    #     return super().form_valid(form)

class SensorAddView(LoginRequiredMixin, CreateView):
    model = Sensor
    template_name = "form.html"
    form_class = SensorForm
    success_url = reverse_lazy("manage")
    #permission_required = "viewer.add_controller"


class SensorView(LoginRequiredMixin, ListView):
    template_name = "sensors.html"
    model = Sensor

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        sensors_for_location = Sensor.objects.filter(controller__location=location_id)
        return sensors_for_location.exclude(status__name='Deleted')
    

class DataView(LoginRequiredMixin, ListView):
    template_name = "data_list.html"
    model = ControllerData

    def get_queryset(self):
        sensor_id = self.kwargs['sensor_id']
        return ControllerData.objects.filter(controller__sensor=sensor_id)


class LocationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('locations')

class ControllerView(LoginRequiredMixin, ListView):
    template_name = "controller_list.html"
    model = Controller
    context_object_name = 'controllers'

    def get_queryset(self):
        return Controller.objects.exclude(status__name='Deleted')

class ControllerUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Controller
    form_class = ControllerCreateForm
    success_url = reverse_lazy('manage')

class SensorUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Sensor
    form_class = SensorForm
    success_url = reverse_lazy('manage')


@method_decorator([login_required, qualification_required], name='dispatch')
class CustomSensorDeleteView(LoginRequiredMixin, DeleteView):
    model = Sensor
    success_url ="/" 
    template_name = "confirm_delete.html"

    def form_valid(self, form, **kwargs):
        sensor_id = self.kwargs['pk']
        object_for_delete = Sensor.objects.filter(id=sensor_id)
        delete_status = Status.objects.get(name="Deleted")
        object_for_delete.update(status=delete_status)
        return HttpResponseRedirect(self.success_url)