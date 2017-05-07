# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#you can do for loops for trainer horse where trainer == trainer
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse
from .models import Horse, Breed, uploadFile, Farrier, Owner, Calendar, farrierForm, Veterinarian, vetForm, farrierCare, Person
#from .forms import farrierForm
from django.forms import inlineformset_factory
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
    all_farriers = Farrier.objects.all()
    for farrier in all_farriers:
        farrier_name = farrier.name
        farrier = Farrier.objects.get(name=farrier_name)
        newFormSet = inlineformset_factory(Farrier, farrierCare, fields={'farrier_actions', 'visit_purpose', 'notes'})
    #aah = newFormSet(instance=farrier)
        if request.method =='POST':
            aah_post = newFormSet(request.POST)
            if aah_post.is_valid():
                new_aah = aah_post.save()
        #aah = newFormSet(instance=farrier)
    return render(request, 'horsehome.html', {'formset':newFormSet})




def index(request):
    user = request.user
    email_address = request.user.email
    poi = Owner.objects.filter(email=email_address)
    print(poi)
    filtered_h = Horse.objects.filter(owner=poi)
    print(filtered_h)
    horses = Horse.objects.all()

    if request.method == 'POST':
        if f.is_valid():
            new_owner = f.save()

    return render(request, 'index.html', context={'horse': horses})
    #farrier = farrierForm(request.POST)
    #new_farrier = farrier.save()


    #owner = Owner.objects.all().count()






    #horse = Horse.objects.all()
    #return render(
    #request, 'horsehome', context={'horses': horse})

def butts(request):
    return HttpResponse("butt")

def veterinarians(request):
    vets = Veterinarian.objects.all()
    if request.method == 'POST':
        v = vetForm(request.POST)
        if v.is_valid():
            new_vet = v.save()
    return render(request, 'veterinarians.html', context={'veterinarian': vets})

#throw scheduler in here
#figure how to get calendar on a per horse or person basis
#profit
