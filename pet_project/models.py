# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.
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

class uploadFile(models.Model):
    description = models.CharField(max_length=300, blank=False)
    document = models.FileField(upload_to='Documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length = 300, blank=False)
    def __str__(self):
        return (self.description)

class Plan(models.Model):
    plan = models.CharField(max_length = 30000)
    author = models.CharField(max_length=300, blank=False)
    file = models.ForeignKey(uploadFile, null="True")
    #add as foreignkey to farrier trainer etc

class Farrier(models.Model):
    name = models.CharField(max_length= 300)
    #horse_name = models.ForeignKey(HorseInfo, default = "None")
    def __str__(self):
        return self.name

class Veterinarian(models.Model):
    name = models.CharField(max_length=300)
    def __str(self):
        return self.name

class Owner(models.Model):
    name = models.CharField(max_length= 300)
    phone_number = models.IntegerField(default=1234567890)
    email = models.CharField(max_length= 200)
    #horse = models.ForeignKey(HorseInfo, on_delete=models.CASCADE)
    def __str__(self):
        return (self.name)

class Trainer(models.Model):
    name = models.CharField(max_length = 300)
#    #horse = models.ForeignKey(HorseInfo, on_delete=models.CASCADE)
    discipline = models.CharField(max_length = 300, default = "None")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length = 300)
    discipline = models.CharField(max_length = 300)
    #training_plans = models.upload a file
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null="True")
    def __str__(self):
        return (self.name)

class Breed(models.Model):
    breed = models.CharField(max_length=300, default='Grade')
    def __str__(self):
        return (self.breed)

class Horse(models.Model):
    #models.ForeignKey(whatever it links to)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
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


class veterinaryCare(models.Model):
    vet_actions = (
        ('RT', 'Routine'),
        ('NC', 'New Complaint'),
        ('FL', 'Followup'),
        ('PP', 'Prepurchase')
    )
    veterinarian = models.ForeignKey(Veterinarian, on_delete=models.CASCADE)
    #horse = models.ForeignKey(Horse, on_delete=models.CASCADE)
    visit_purpose = models.CharField(choices = vet_actions, max_length=1)
    attachments = models.ForeignKey(uploadFile, on_delete=models.CASCADE, null="True")


class Calendar(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=False)
    vet_care = models.ForeignKey(veterinaryCare, on_delete=models.CASCADE, null="True")
