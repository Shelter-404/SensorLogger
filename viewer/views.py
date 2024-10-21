from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm, ControllerCreateForm, SensorForm, LocationForm
from .models import Location, Status, Sensor, Controller, ControllerData
from .decorators import qualification_required

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


@method_decorator([login_required, qualification_required], name='dispatch')
class LocationAddView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = "form.html"
    success_url = reverse_lazy("manage")



@method_decorator([login_required, qualification_required], name='dispatch')
class ControllerAddView(CreateView):
    model = Controller
    form_class = ControllerCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("manage")


@method_decorator([login_required, qualification_required], name='dispatch')
class SensorAddView(CreateView):
    model = Sensor
    template_name = "form.html"
    form_class = SensorForm
    success_url = reverse_lazy("manage")



class SensorView(LoginRequiredMixin, ListView):
    template_name = "sensors.html"
    model = Sensor

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        sensors_for_location = Sensor.objects.filter(controller__location=location_id)
        sensors_to_show = sensors_for_location.exclude(status__name='Deleted')
        print(sensors_to_show)
        return sensors_to_show




class DataView(LoginRequiredMixin, ListView):
    template_name = "data_list.html"
    model = ControllerData
    context_object_name = 'obj_list'

    def get_queryset(self):
        sensor_id = self.kwargs['pk']
        return ControllerData.objects.filter(controller__sensor=sensor_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sensor_id = self.kwargs['pk']
        sensor = Sensor.objects.get(id=sensor_id)
        context['name_sensor'] = sensor.name
        return context



@method_decorator([login_required, qualification_required], name='dispatch')
class LocationUpdateView(UpdateView):
    template_name = 'form.html'
    model = Location
    form_class = LocationForm
    success_url = reverse_lazy('locations')


@method_decorator([login_required, qualification_required], name='dispatch')
class CustomLocationDeleteView(DeleteView):
    model = Location
    success_url ="/"
    template_name = "confirm_delete.html"

    def form_valid(self, form, **kwargs):
        location_id = self.kwargs['pk']
        object_for_delete = Location.objects.filter(id=location_id)
        delete_status = Status.objects.get(name="Deleted")
        object_for_delete.update(status=delete_status)
        return HttpResponseRedirect(self.success_url)


class ControllerView(LoginRequiredMixin, ListView):
    template_name = "controller_list.html"
    model = Controller
    context_object_name = 'controllers'

    def get_queryset(self):
        return Controller.objects.exclude(status__name='Deleted')

@method_decorator([login_required, qualification_required], name='dispatch')
class ControllerUpdateView(UpdateView):
    template_name = 'form.html'
    model = Controller
    form_class = ControllerCreateForm
    success_url = reverse_lazy('manage')

@method_decorator([login_required, qualification_required], name='dispatch')
class SensorUpdateView(UpdateView):
    template_name = 'form.html'
    model = Sensor
    form_class = SensorForm
    success_url = reverse_lazy('manage')


@method_decorator([login_required, qualification_required], name='dispatch')
class CustomSensorDeleteView(DeleteView):
    model = Sensor
    success_url ="/" 
    template_name = "confirm_delete.html"

    def form_valid(self, form, **kwargs):
        sensor_id = self.kwargs['pk']
        object_for_delete = Sensor.objects.filter(id=sensor_id)
        delete_status = Status.objects.get(name="Deleted")
        object_for_delete.update(status=delete_status)
        return HttpResponseRedirect(self.success_url)


