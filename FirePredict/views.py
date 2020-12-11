from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def firedata_detail(request):
    fire_data = models.FireData.objects.all()
    #fwi = fire_data.fire_weather_index
    #date = fire_data.date
    content = {}
    content['f_obj'] = fire_data
    return render(request,'fireDetail.html',content)