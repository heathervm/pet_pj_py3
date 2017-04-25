# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#you can do for loops for trainer horse where trainer == trainer
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse
from .models import Horse, Breed, uploadFile, Farrier, Owner, Calendar, farrierForm
#from .forms import farrierForm

from django.shortcuts import render_to_response, get_object_or_404

from django.template import RequestContext

from django.core.urlresolvers import reverse
from django.forms import ModelForm
#class horseListView(generic.ListView):
#    model = Horse
#    def get_queryset(self):
#        return Horse.objects.filter(owner__icontains='H')

def farriers(request):
    all_farriers = Farrier.objects.all()
    if request.method == 'POST':
        f = farrierForm(request.POST)
        if f.is_valid():
            new_farrier = f.save()
            print("Farrier successfully updated")
    return render(request, 'farriers.html', context={'farrier': all_farriers})

def horsehome(request):
    return render(request, 'horsehome.html')




def index(request):
    horses = Horse.objects.all()
    if request.method == 'POST':
        if f.is_valid():
            new_horse = f.save()

    return render(request, 'index.html', context={'horse': horses})
    #farrier = farrierForm(request.POST)
    #new_farrier = farrier.save()


    #owner = Owner.objects.all().count()






    #horse = Horse.objects.all()
    #return render(
    #request, 'horsehome', context={'horses': horse})

def butts(request):
    return HttpResponse("butt")

