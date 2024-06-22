from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import SignUpForm, LocationForm
from .models import Location, Status, Sensor, Controller, ControllerData
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class SignUpView(CreateView):
    template_name = "form.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home")

class StartView(View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="index.html")

class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, template_name="homepage.html")

class LocationView(LoginRequiredMixin, ListView):
    template_name = "locations.html"
    model = Location
    #permission_required = "viewer.view_location"

class LocationAddView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['name', 'description']
    template_name = "form.html"
    success_url = reverse_lazy("locations")
    # permission_required = "viewer.add_location"

    def form_valid(self, form):
        # Create a new Status object
        status = Status.objects.create(
            added_by=self.request.user,
            modified_by=self.request.user
        )
        # Assign the created status to the location
        form.instance.status = status
        return super().form_valid(form)

class SensorView(LoginRequiredMixin, ListView):
    template_name = "sensors.html"
    model = Sensor

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return Sensor.objects.filter(controller__location=location_id)

class DataView(LoginRequiredMixin, ListView):
    template_name = "data_list.html"
    model = ControllerData

    def get_queryset(self):
        sensor_id = self.kwargs['sensor_id']
        return ControllerData.objects.filter(controller__sensor=sensor_id)