from __future__ import unicode_literals
import datetime
from django.forms import modelform_factory, ModelForm
from django.db import models
#from django.forms import Calendar

# Create your models here.
from django.core.validators import RegexValidator

from .model_chow import *


class Person(models.Model):
    name = models.CharField(max_length=300, blank=False, default="Jane Doe")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, default='8008888888', max_length=15)
    address = models.CharField(max_length = 700, blank= "True")
    email = models.EmailField(max_length=100, blank="True")
    #account = models.ForeignKey(Account, on_delete=models.CASCADE, blank="True", null="True")
    def __str__(self):
        return (self.name)

class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False)
    owner = models.ForeignKey(Person, blank=False, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, default='8008888888', max_length=15)
    address = models.CharField(max_length = 700, blank= "True")
    email = models.EmailField(max_length=100, blank="True")

class Account(models.Model):
    
    creditor = models.ForeignKey(Person, blank="true", null="True", on_delete=models.CASCADE, related_name='+')
    debtor = models.ForeignKey(Person, blank="true", null="True", on_delete=models.CASCADE, related_name='+')
    amount = models.DecimalField(max_digits = 6, decimal_places=2, null="True")
    description = models.CharField(max_length= 50, null="True")
    def __str__(self):
        return (description)

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

    
class Trainer(models.Model):
    name = models.ForeignKey(Person, null="False", on_delete=models.CASCADE)
    #email = models.EmailField(max_length= 254, null = "True")
#    #horse = models.ForeignKey(HorseInfo, on_delete=models.CASCADE)
    #discipline = models.CharField(max_length = 300, default = "None")
    organization = models.ForeignKey(Organization, blank = "True", null="True", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

