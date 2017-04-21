# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#you can do for loops for trainer horse where trainer == trainer
from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.http import HttpResponse
from .models import Horse, Breed, uploadFile, Farrier, Owner

#class horseListView(generic.ListView):
#    model = Horse
#    def get_queryset(self):
#        return Horse.objects.filter(owner__icontains='H')

def horsehome(request):
    return HttpResponse("horse home index")

def index(request):
    horse = Horse.objects.all()
    horse_name = horse
    print("welcome to index home")
    owner = Owner.objects.all().count()
    return render(request, 'index.html', context={'horse': horse_name, 'owner':owner})



    #horse = Horse.objects.all()
    #return render(
    #request, 'horsehome', context={'horses': horse})

def butts(request):
    return HttpResponse("butt")
