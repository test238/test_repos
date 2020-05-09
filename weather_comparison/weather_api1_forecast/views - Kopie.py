from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import requests
from .models import City, City2
from .forms import CityForm

def index(request):
    cities = City.objects.all() #return all the cities in the database
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f3d77950bc7cc4a4899f21e0e491ecd3'

    if request.method == 'POST': # only true if form is submitted
        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate
    form = CityForm()
    
    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types
    
        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current city into our list
        
    context = {'weather_data' : weather_data, 'form' : form}  
    return render(request, 'weather_api1_forecast/index.html', context) #returns the index.html template
