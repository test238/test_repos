from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from .unit_converter import parse_dms
import re

def index(request):
    cities = City.objects.all() #return all the cities in the database
    #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f3d77950bc7cc4a4899f21e0e491ecd3'

    url = 'https://api.opencagedata.com/geocode/v1/json?q={}&key=1e73e20428e54172a2795c05a59cafab'
    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()

    weather_data = []
    
    for city in cities:
        city_geodata = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    
        weather = {
            'city' : city,
            'temperature' : parse_dms(city_geodata["results"][0]["annotations"]["DMS"]["lat"]),
            'description' : parse_dms(city_geodata["results"][0]["annotations"]["DMS"]["lng"]),
            #'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list
        
    context = {'weather_data' : weather_data, 'form' : form}  
    return render(request, 'weather_api1_forecast/index.html', context) #returns the index.html template
