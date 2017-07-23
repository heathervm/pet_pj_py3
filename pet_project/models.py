# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.forms import modelform_factory, ModelForm
from django.db import models
#from django.forms import Calendar

# Create your models here.
from django.core.validators import RegexValidator

class Brand(models.Model):
    brand = models.CharField(max_length=300)
    country_of_origin = models.CharField(max_length=300, default = "United States")
    def __str__(self):
        return (self.brand)

class Grain(models.Model):
    name = models.CharField(max_length = 300)
    brand = models.CharField(max_length = 200)
    energy_level = models.CharField(max_length = 300, default = "Medium")
    brand = models.ForeignKey(Brand, null="True")
    def __str__(self):
        return (self.name)

class Supplements(models.Model):
    name = models.CharField(max_length=300)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)
    days_ordered = models.IntegerField(blank="True", default=30)

class Clinic(models.Model):
    name = models.CharField(max_length=300, blank=False, default="SOP")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, default='8008888888', max_length=15)
    address = models.CharField(max_length = 700, blank= "True")
    email = models.EmailField(max_length=100, blank="True")
    def __str__(self):
        return (self.name)
    
class Person(models.Model):
    name = models.CharField(max_length=300, blank=False, default="Jane Doe")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, default='8008888888', max_length=15)
    address = models.CharField(max_length = 700, blank= "True")
    email = models.EmailField(max_length=100, blank="True")
    def __str__(self):
        return (self.name)

class uploadFile(models.Model):
    description = models.CharField(max_length=300, blank=False)
    document = models.FileField(upload_to='Documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Person, blank=False)
    def __str__(self):
        return (self.description)

class Plan(models.Model):
    plan = models.CharField(max_length = 30000)
    author = models.ForeignKey(Person, blank=False)
    file = models.ForeignKey(uploadFile, null="True")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    #add as foreignkey to farrier trainer etc


class Farrier(models.Model):
    #leave alone til more time to play with but change to person
    name = models.CharField(max_length=300, null="False")
    email = models.EmailField(max_length= 254, null="True")
    phone_number = models.IntegerField(default=1234567890)
    #horse_name = models.ForeignKey(HorseInfo, default = "None")
    def __str__(self):
        return (self.name)

class Veterinarian(models.Model):
    name = models.ForeignKey(Person, null="False", on_delete=models.CASCADE)
    clinic = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)
    #phone_number = models.IntegerField(default=1234567890)
    #email = models.EmailField(max_length= 254, null="True")
    def __str(self):
        return self.name

class Owner(models.Model):
    #same
    name = models.CharField(max_length= 300)
    phone_number = models.IntegerField(default=1234567890)
    email = models.EmailField(max_length= 254, null = "True")
    #horse = models.ForeignKey(HorseInfo, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)

class Trainer(models.Model):
    name = models.ForeignKey(Person, null="False", on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, null="True", blank="True", on_delete=models.CASCADE)
    #email = models.EmailField(max_length= 254, null = "True")
#    #horse = models.ForeignKey(HorseInfo, on_delete=models.CASCADE)
    #discipline = models.CharField(max_length = 300, default = "None")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE, null="False")
    #discipline = models.CharField(max_length = 300)
    #email = models.EmailField(max_length= 254, null = "True")
    #phone_number = models.IntegerField(default=1234567890)
    #training_plans = models.ForeignKey(Plan)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null="True")
    def __str__(self):
        return (self.name)

class Breed(models.Model):
    breed = models.CharField(max_length=300, default='Grade')
    def __str__(self):
        return (self.breed)

class Horse(models.Model):
    #models.ForeignKey(whatever it links to)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length= 300)
    age = models.DateTimeField(auto_now_add=True, blank=True)
    breed = models.ForeignKey(Breed, null="True", on_delete=models.CASCADE)
    #allergies = models.ForeignKey(Allergies)
    grain = models.ForeignKey(Grain, null="True") #make this a dropdown in time
    farrier = models.ForeignKey(Farrier, null="True", on_delete=models.CASCADE)
    #discipline = models.ForeignKey(Trainer.discipline, default = "None", nul="None")
#    supplements = models.CharField(max_length = 300, default = "None") #same
    photo = models.ForeignKey(uploadFile, null="True", on_delete=models.CASCADE)

    #trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default="None")
    def __str__(self):
        return self.name

#class Training(models.Model):
#    date = models.DateTimeField(blank=False, editable=True)
#    horse = models.foreignKey(Horse, on_delete=models.CASCADE, null=True, blank=True)
#    rider = models.foreignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
#    notes = models.foreignKey(Plan, on_delete=models.CASCADE, null=True, blank=True)
    
    
class veterinaryCare(models.Model):
    vet_actions = (
        ('RT', 'Routine'),
        ('NC', 'New Complaint'),
        ('FL', 'Followup'),
        ('PP', 'Prepurchase')
    )
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)

    #horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    visit_purpose = models.CharField(choices = vet_actions, max_length=2)
    attachments = models.ForeignKey(uploadFile, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.CharField(max_length = 1000, blank="True")

class farrierCare(models.Model):
    farrier_actions = (
    ('TR', 'Trim'),
    ('FS', 'Front shoes'),
    ('BS', 'Back shoes'),
    ('AS', 'All four shoes'),
    ('Alum', 'Aluminum shoes'),
    ('Steel', 'Steel shoes'),
    ('Spec', 'Specialty shoes')
    )
    farrier = models.ForeignKey(Farrier, on_delete = models.CASCADE)
    visit_purpose = models.CharField(choices = farrier_actions, max_length = 2)
    notes = models.CharField(max_length=1000, blank="True", null=True)

class Calendar(models.Model):
    date = models.DateTimeField(blank="False", editable="True")
    vet_care = models.ForeignKey(veterinaryCare, on_delete=models.CASCADE, null=True, blank=True)
    farrier_care = models.ForeignKey(farrierCare, on_delete=models.CASCADE, null=True, blank=True)
    horse = models.ForeignKey(Horse, on_delete=models.CASCADE, null = "True")


    
class farrierForm(ModelForm):
    class Meta:
        model = Farrier
        fields = ['name', 'email', 'phone_number']

#CalendarForm = modelform_factory(Calendar, fields=('date', 'vet_care', 'farrier_care'))
class vetForm(ModelForm):
    class Meta:
        model = Veterinarian
        fields = ['name']

#class farrierCareForm(ModelForm):
#    class Meta:
#        fields=['farrier_actions', 'farrier', 'visit_purpose', 'notes']


