from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView
from .forms import SignUpForm
from .models import Location
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
    #permission_required = "viewer.view_locations"