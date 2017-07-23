# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#you can do for loops for trainer horse where trainer == trainer
from django.shortcuts import render
import datetime
#import schedule
# Create your views here.
from django.views import generic
from django.http import HttpResponse
from .models import Horse, Breed, uploadFile, Farrier, Veterinarian, vetForm, farrierCare, Person, farrierForm #Calendar
#from .forms import farrierForm
from django.forms import inlineformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
#from django.template import RequestContext
#from schedule.models import Calendar
#from schedule.models import Event
#from schedule.models import Rule

#from schedule.settings import GET_EVENTS_FUNC, OCCURRENCE_CANCEL_REDIRECT

from django.core.urlresolvers import reverse
from django.forms import ModelForm
#from schedule.forms import EventForm, OccurrenceForm
#from schedule.models import Calendar, Occurrence, Event
#from schedule.periods import weekday_names
#from schedule.utils import check_event_permissions, coerce_date_dict


#class horseListView(generic.ListView):
#    model = Horse
#    def get_queryset(self):
#        return Horse.objects.filter(owner__icontains='H')

#VIEWS TO HAVE INSTEAD OF A MESS

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


def horsename(request, name):
    #try:
        #horse_name = Horses.objects.get(name=name)
    #except:
        #pass
    #or
    from .models import Horse 
    pony = get_object_or_404(Horse, name=name)
    return render(request, 'horsename.html',{'pony':pony})
#then it's /pet_project/templates/horsename.html

def index(request):
    rule = Rule(frequency="YEARLY", name="Yearly", description="will recur once every Year")
    rule.save()
    rule = Rule(frequency="WEEKLY", name="Weekly", description="will recur once every Week")
    rule.save()
    user = request.user
    email_address = request.user.email
    poi = Person.objects.filter(email=email_address)
    #print(poi)
    filtered_h = Horse.objects.filter(owner=poi)
    #print(filtered_h)
    horses = Horse.objects.all()
    
    today = datetime.date.today()
    try: 
        cal = get_object_or_404(Calendar, slug="test4")
        print(cal)
    except: 
        cal = Calendar(name="test cal4", slug="test4")
        cal.save()
        data = {
            'title': 'test other other',
            'start': datetime.datetime(today.year, 5, 25, 19, 30),
            'end': datetime.datetime(today.year, 5, 25, 23, 55),
            'end_recurring_period': datetime.datetime(today.year, 5, 26, 1, 1),
            'calendar': cal
        }
        event = Event(**data)
        print(event)
        event.save()
    test_cal = Calendar(request, 'test4', 'index.html')   
    #def calendar_by_periods(request, test4, periods=None,                                   template_name="schedule/index.html"):
    
    
        #calendar = get_object_or_404(Calendar, slug="test4")
        #try:
        #    date = coerce_date_dict(request.GET)
        #except ValueError:
        #    raise Http404

        #if date:
        #    try:
        #        date = datetime.datetime(**date)
        #    except ValueError:
        #        raise Http404
        #else:
        #    date = timezone.now()
        #event_list = GET_EVENTS_FUNC(request, calendar)
        #period_objects = dict([(period.__name__.lower(), period(event_list, date)) for period in periods])
        #return render_to_response(template_name, {
        #    'date': date,
        #    'periods': period_objects,
        #    'calendar': calendar,
        #    'weekday_names': weekday_names,
        #    'here': quote(request.get_full_path()),
        #}, context_instance=RequestContext(request), )
    
    #calendar(request, "test4", 'index.html')

    #print(cal)
    #for horse in cal:
    #    print(horse)

    #    cal_list = []
    #    vet_obj = horse.vet_care
    #    cal_list.append(vet_obj)
    #    print (cal_list)
    #    np = Month(cal_list, timezone.now)

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
    
def every_person(request):
    all_peeps = Person.objects.all()
    peep_name_list = []
    peep_url_list = []
    for peep in all_peeps:
        peep_id = peep.id
        
        peep_name = peep.name
        peep_name_list.append(peep_id)
        peep_url = str(peep.id)+'/info'
        peep_url_list.append(peep_url)
    return render(request, 'every_person.html', {'every_person': peep_name_list}, {'peep_url': peep_url_list})
                  
def person(request, person_id):
    #all_peeps = Person.objects.all()
    if request.user.is_superuser:
        try:
        
            poi = Person.objects.filter(id = person_id)
            print(poi)
            print("ok")
            print(request.user.id)
        except:
            print("unknown person")
            pass
        return render(request, 'person.html', {'poi': poi})

    else:
        return render(request, 'index.html')

def veterinarians(request):
    vets = Veterinarian.objects.all()
    if request.method == 'POST':
        v = vetForm(request.POST)
        if v.is_valid():
            new_vet = v.save()
    return render(request, 'veterinarians.html', context={'veterinarian': vets})

#def lessonplan(request, person_id):
    
    #plans = lessonPlan.objects.all()
    #user = user.id
    #print(user.id)
    
#throw scheduler in here
#figure how to get calendar on a per horse or person basis
#profit

#The Week period is instantiated with a list of events and a date or datetime object. It resembles the week that contains the date or datetime object that was passed in.
#p = Week(events, datetime.datetime(2008,4,1))
# p.start
#datetime.datetime(2008, 3, 30, 0, 0)
# p.end
#datetime.datetime(2008, 4, 6, 0, 0)
# -Remember start is inclusive and end is exclusive
