from .models import Report, Person, Vehicle, Ticket
from django.forms import ModelForm


class NoteForm(ModelForm):
    class Meta:
        model = Report
        fields = ['person', 'notes']

class PersonCreate(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class VehicleCreate(ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'

class TicketCreate(ModelForm):
    class Meta:
        model = Ticket
        fields = ['vehicle', 'offence', 'location']
