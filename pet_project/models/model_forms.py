from .model_people import *

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
