from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField, Textarea, ModelChoiceField
from django.db.transaction import atomic
from django.contrib.auth import get_user_model
from .models import Location, Status, Controller, Sensor

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', "first_name", 'email']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        return super().save(commit)


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["status"].queryset = Status.objects.exclude(name="Deleted")


class ControllerCreateForm(ModelForm):
    class Meta:
        model = Controller
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["location"].queryset = Location.objects.exclude(status__name="Deleted")
        self.fields["status"].queryset = Status.objects.exclude(name="Deleted")

class SensorForm(ModelForm):
    class Meta:
        model = Sensor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["controller"].queryset = Controller.objects.exclude(status__name="Deleted")
        self.fields["status"].queryset = Status.objects.exclude(name="Deleted")



































