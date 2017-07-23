
from __future__ import unicode_literals
import datetime
from django.forms import modelform_factory, ModelForm
from django.db import models
#from django.forms import Calendar

# Create your models here.
from django.core.validators import RegexValidator

from .model_people import *
from .model_chow import *
#from .model_utilites import *


class Breed(models.Model):
    breed_primary = models.CharField(max_length=100, blank="True")
    breed_secondary = models.CharField(max_length=100, blank="True")
    def __str__(self):
        return self.breed_primary

class Allergies(models.Model):
    allergy_primary = models.CharField(max_length=100, blank="True")
    allergy_secondary = models.CharField(max_length=100, blank="True")
    allergy_tertiary = models.CharField(max_length=100, blank="True")
    def __str__(self):
        return self.allergy_primary
    
class Horse(models.Model):
    #models.ForeignKey(whatever it links to)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length= 300)
    age = models.DateTimeField(auto_now_add=True, blank=True)
    breed = models.ForeignKey(Breed, null="True", on_delete=models.CASCADE)
    allergies = models.ForeignKey(Allergies, null="True", blank="True", on_delete=models.CASCADE)
    grain = models.ForeignKey(Grain, null="True") #make this a dropdown in time
    farrier = models.ForeignKey(Farrier, null="True", on_delete=models.CASCADE)
    #discipline = models.ForeignKey(Trainer.discipline, default = "None", nul="None")
#    supplements = models.CharField(max_length = 300, default = "None") #same
    photo = models.ForeignKey(uploadFile, null="True", on_delete=models.CASCADE)

    #trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, default="None")
    def __str__(self):
        return self.name

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


    