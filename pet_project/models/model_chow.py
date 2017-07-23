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
    def __str__(self):
        return (self.name)