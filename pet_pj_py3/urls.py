"""pet_pj_py3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf.urls.static import static
from pet_project import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^horsehome/$', views.horsehome, name = 'horse_home'),
    url(r'^farriers/$', views.farriers, name='farriers'),
    url(r'^veterinarians/$', views.veterinarians, name='veterinarians'),
    url(r'^(?P<person_id>[0-9]+)/info/$', views.person, name='person'),
    url(r'^every_person/$', views.every_person, name='every_person'),
    url(r'^(?P<name>w+)/info$', views.horsename, name = 'horsename'),
]

#urlpatterns += [
    #url(r'^$', RedirectView.as_view(url='/index/', permanent=True)),
    #url(r'^$', RedirectView.as_view(url='/horsehome/', permanent=True))
#]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
