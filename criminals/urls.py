from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'criminals'

urlpatterns = [
    # home
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),

    # user profile
    url(r'^profile$', login_required(views.profile_view), name='profile'),

    # persons-of-interest
    url(r'^persons_of_interest$', login_required(views.persons_of_interest), name='persons_of_interest'),

    # vehicles
    url(r'^vehicles$', login_required(views.vehicles), name='vehicles'),

    # /criminals/71/ (persons)
    url(r'^persons/(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),

    url(r'^vehicles/(?P<pk>[0-9]+)/$', login_required(views.VehicleDetailView.as_view()), name='vehicle-detail'),

    # /criminal/add-note
    url(r'^add-note/$', login_required(views.NoteCreateView.as_view()), name='note-add'),

    # /criminal/add-person
    url(r'^add-person/$', login_required(views.PersonCreateView.as_view()), name='person-add'),

    # /criminal/add-vehicle
    url(r'^add-vehicle/$', login_required(views.VehicleCreateView.as_view()), name='vehicle-add'),

    # /criminal/add-ticket
    url(r'^add-ticket/$', login_required(views.TicketCreateView.as_view()), name='ticket-add'),

    # /search_results
    url(r'^vehicles_search$', views.VehicleSearch.as_view(), name='vehicle-result'),
    url(r'^persons_search$', views.PersonSearch.as_view(), name='person-search'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
