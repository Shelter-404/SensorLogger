"""
URL configuration for sensor_logger project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
import django.contrib.auth.views as auth_views
from viewer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/signup/', views.SignUpView.as_view(), name="signup"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', lambda request: redirect('index', permanent=False)),
    path('index/', TemplateView.as_view(template_name="index.html"), name="index"),
    path('home/', TemplateView.as_view(template_name="homepage.html"), name="home"),
    # path('home/manage', views.ManageView.as_view(), name="manage"), reserved for future
    path('home/manage', TemplateView.as_view(template_name="management.html"), name="manage"),
    path('manage/controller', views.ControllerView.as_view(), name="controller_list"),
    path('locations/', views.LocationView.as_view(), name="locations"),
    path('add/location', views.LocationAddView.as_view(), name='add_location'),
    path('sensors/<int:location_id>', views.SensorView.as_view(), name='sensors'),
    path('sensors/data/<int:pk>', views.DataView.as_view(), name='data'),
    path('add/controller', views.ControllerAddView.as_view(), name='add_controller'),
    path('add/sensor', views.SensorAddView.as_view(), name='add_sensor'),
    path('edit/location/<int:pk>', views.LocationUpdateView.as_view(), name='edit_location'),
    path('edit/controller/<int:pk>', views.ControllerUpdateView.as_view(), name='edit_controller'),
    path('edit/sensor/<int:pk>', views.SensorUpdateView.as_view(), name='edit_sensor'),
    path('delete/sensor/<int:pk>', views.CustomSensorDeleteView.as_view(), name='delete_sensor'),
]
