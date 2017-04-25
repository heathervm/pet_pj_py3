#forms go here
from django.forms import modelform_factory, ModelForm
from django.db import models
from .models import uploadFile, Horse, Farrier, Owner, Breed, Grain, Veterinarycare, Calendar

class farrierForm(ModelForm):
    class Meta:
        model = Farrier
        fields = ['name']

#class CalendarForm(ModelForm):
#    class Meta:
#        model = Calendar

  #      fields = ['horse', 'date', 'vet_care', 'farrier_care']
