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
import django.contrib.auth.views as auth_views
from viewer.views import SignUpView, StartView, HomeView, LocationView, LocationAddView, SensorView, DataView, ControllerAddView, SensorAddView, ManageView, LocationUpdateView
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/signup/', SignUpView.as_view(), name="signup"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', lambda request: redirect('index', permanent=False)),
    path('index/', StartView.as_view(), name="index"),
    path('home/', HomeView.as_view(), name="home"),
    path('home/manage', ManageView.as_view(), name="manage"),
    path('locations/', LocationView.as_view(), name="locations"),
    path('add/location', LocationAddView.as_view(), name='add_location'),
    path('sensors/<int:location_id>', SensorView.as_view(), name='sensors'),
    path('sensors/data/<int:sensor_id>', DataView.as_view(), name='data'),
    path('add/controller', ControllerAddView.as_view(), name='add_controller'),
    path('add/sensor', SensorAddView.as_view(), name='add_sensor'),
    path('edit/location/<int:pk>', LocationUpdateView.as_view(), name='edit_location'),
]
