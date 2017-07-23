# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from .models import uploadFile, Horse, Farrier, Breed, Grain, veterinaryCare, Lesson, farrierCare, Person, Veterinarian #CalendarForm, Calendar
admin.site.register(uploadFile)
admin.site.register(Horse)
admin.site.register(Farrier)
#admin.site.register(Owner)
admin.site.register(Breed)
admin.site.register(Grain)
admin.site.register(veterinaryCare)
#admin.site.register(Calendar)
admin.site.register(Lesson)
admin.site.register(farrierCare)
admin.site.register(Person)
admin.site.register(Veterinarian)
