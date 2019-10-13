from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# If making changes in code,
# Step 1: in terminal, type py manage.py makemigrations criminals
# Step 2: in terminal, type py manage.py migrate

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, default='', editable=True)
    gender = models.CharField(max_length=6)
    photo = models.FileField()
    dob = models.CharField(max_length=12, default='dd/mm/yyyy', editable=True)
    address = models.CharField(max_length=255, default='', editable=True)
    city = models.CharField(max_length=255, default='', editable=True)
    permit = models.CharField(max_length=11)
    notes = models.CharField(max_length=2000, default='', editable=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName + ' - ' + self.permit

class Offence(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    offence = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='N/A', editable=True)

    def __str__(self):
        return self.person.firstName + " " + self.person.lastName + " - " + self.offence

class Desc(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    height = models.CharField(max_length=50, default='', editable=True)
    build = models.CharField(max_length=20, default='', editable=True)
    hair = models.CharField(max_length=20, default='', editable=True)
    eyes = models.CharField(max_length=20, default='', editable=True)
    teeth = models.CharField(max_length=20, default='', editable=True)
    weight = models.CharField(max_length=3, default='', editable=True)
    complexion = models.CharField(max_length=20, default='', editable=True)
    facial_hair = models.CharField(max_length=20, default='', editable=True)
    tattoo = models.CharField(max_length=20, default='', editable=True)
    scars = models.CharField(max_length=20, default='', editable=True)
    face_shape = models.CharField(max_length=20, default='', editable=True)

    def get_absolute_url(self):
        return reverse('criminals:detail', kwargs={'pk': self})

    def __str__(self):
        return self.person.firstName + ' ' + self.person.lastName + ": " + self.person.permit


class Report(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    notes = models.TextField(max_length=2000)

    def get_absolute_url(self):
        return reverse('criminals:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.person.permit + ' - ' + self.person.firstName + ' ' + self.person.lastName

class Vehicle(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    dp = models.CharField(max_length=7)
    car_make = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_year = models.CharField(max_length=4)
    license_plate = models.CharField(max_length=7)

    def __str__(self):
        return self.license_plate + ' - ' + self.owner.firstName + ' ' + self.owner.lastName

class TrafficOffence(models.Model):
    traffic_offence = models.CharField(max_length=100)
    enactment = models.CharField(max_length=200)
    fixed_penalty = models.CharField(max_length=10)
    penalty_points = models.CharField(max_length=3)

    def __str__(self):
        return self.traffic_offence

class Ticket(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    ticket_date = models.DateTimeField(auto_now=True)
    offence = models.ForeignKey(TrafficOffence, on_delete=models.CASCADE)
    date_time_of_offence = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle.license_plate + ' at ' + self.location
