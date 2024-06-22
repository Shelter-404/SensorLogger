from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField, Textarea
from django.db.transaction import atomic
from .models import Location, Status

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username', "first_name", 'email']

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        return super().save(commit)


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = "name", "description"

    name = CharField()
    description = Textarea()





































