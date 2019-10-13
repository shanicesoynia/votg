from django.contrib import admin
from . models import Person, Desc, Offence, Report, Vehicle, Ticket, TrafficOffence

admin.site.register(Person)
admin.site.register(Desc)
admin.site.register(Offence)
admin.site.register(Report)
admin.site.register(Vehicle)
admin.site.register(Ticket)
admin.site.register(TrafficOffence)
