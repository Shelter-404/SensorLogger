from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CharField, Textarea, ModelChoiceField
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


    #status_name = ModelChoiceField(queryset=Status.objects.all())
    # status_name = CharField(max_length=3)
    name = CharField()
    description = Textarea()
    class Meta:
        model = Location
        fields = ["name", "description", 'status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance and self.instance.status:
    #         self.fields['status_name'].initial = self.instance.status.name
    #
    # def save(self):
    #     location = super().save(commit=False)
    #     print(location)
    #     status_name = self.cleaned_data['status_name']
    #     print(status_name)
    #
    #     status = location.status
    #     print(status)
    #     status.name = status_name
    #     status.save()
    #     location.save()
    #
    #     return location









































