from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.edit import CreateView
from .models import Person, Desc, Offence, Report, Ticket, Vehicle, TrafficOffence
from django.core.paginator import Paginator
from .forms import NoteForm, PersonCreate, VehicleCreate, TicketCreate


class IndexView(generic.ListView):
    template_name = 'criminals/index.html'
    context_object_name = 'all_persons'

    def get_queryset(self):
        return Person.objects.all()


class VehicleView(generic.ListView):
    template_name = 'criminals/pages/vehicles.html'
    context_object_name = 'vehicle'

    def get_queryset(self):
        return Vehicle.objects.all()


class DetailView(generic.DetailView):
    model = Person
    template_name = 'criminals/pages/details.html'

class VehicleDetailView(generic.DetailView):
    model = Vehicle
    template_name = 'criminals/pages/vehicle-details.html'

class PersonSearch(generic.ListView):
    model = Person
    template_name = 'criminals/pages/search_results.html'
    context_object_name = 'search_db'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Person.objects.filter(
            Q(firstName__icontains=query) |
            Q(lastName__icontains=query) |
            Q(dob__icontains=query) |
            Q(alias__icontains=query)
        )
        return object_list


class VehicleSearch(generic.ListView):
    model = Vehicle
    template_name = 'criminals/pages/search_results.html'
    context_object_name = 'search_db'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Vehicle.objects.filter(
            Q(license_plate__startswith=query) |
            Q(car_make__startswith=query) |
            Q(car_model__startswith=query) |
            Q(car_year__startswith=query)
        )
        return object_list

# creating a view for Notes
class NoteCreateView(CreateView):
    template_name = 'criminals/note_form.html'  # defining the template
    form_class = NoteForm  # defining the type of form that needed to be used
    success_url = reverse_lazy('criminals:persons_of_interest')  # page redirect


class PersonCreateView(CreateView):
    template_name = 'criminals/pages/createPerson.html'
    form_class = PersonCreate
    success_url = reverse_lazy('criminals:persons_of_interest')


class VehicleCreateView(CreateView):
    template_name = 'criminals/pages/createVehicle.html'
    form_class = VehicleCreate
    success_url = reverse_lazy('criminals:vehicles')


class TicketCreateView(CreateView):
    template_name = 'criminals/pages/createTicket.html'
    form_class = TicketCreate
    success_url = reverse_lazy('criminals:vehicles')


def profile_view(request):
    return render(request, 'criminals/pages/profile.html')


def persons_of_interest(request):
    # retrieving related objects
    individuals = Person.objects.all()
    desc = Desc.objects.all()
    offence = Offence.objects.all()
    report = Report.objects.all()
    ticket = Ticket.objects.all()
    vehicle = Vehicle.objects.all()
    # paginator
    paginator = Paginator(individuals, 6)
    page = request.GET.get('page')
    person = paginator.get_page(page)
    # custom dictionary
    context = {
        'all_persons': person,
        'desc': desc,
        'offence': offence,
        'report': report,
        'ticket': ticket,
        'vehicle': vehicle
    }
    # rendered results of request
    return render(request, 'criminals/pages/persons_of_interest.html', context=context)


def vehicles(request):
    ticket = Ticket.objects.all()
    person = Person.objects.all()
    traffic_offence = TrafficOffence.objects.all()
    all_vehicles = Vehicle.objects.all()
    paginator = Paginator(all_vehicles, 12)
    page = request.GET.get('page')
    vehicle = paginator.get_page(page)

    context = {
        'ticket': ticket,
        'vehicle': vehicle,
        'person': person,
        'traffic_offence': traffic_offence
    }

    return render(request, 'criminals/pages/vehicles.html', context=context)
