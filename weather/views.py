from django.shortcuts import render
from .models import WeatherData
from .utils import fetch_weather_data
from datetime import timedelta
from django.utils import timezone
from django.db.models import Avg

def weather_update(request):
    
    """

        Description : Pass the city name in query params
        Query_params: city
        Example: city= Bangalore
        Returns: Weather information of the city

    """
    
    city = request.GET.get('city', 'Bangalore')

    data = fetch_weather_data(city)
    
    # Store the data
    WeatherData.objects.create(
        city=data['city'],
        temperature=data['temperature'],
        humidity=data['humidity'],
        description=data['description'],
        timestamp=timezone.now()
    )
    
    # Fetch data for trends
    recent_data = WeatherData.objects.filter(
        timestamp__gte=timezone.now() - timedelta(hours=24)
    )
    
    avg_temp = recent_data.aggregate(Avg('temperature'))['temperature__avg']
    avg_humidity = recent_data.aggregate(Avg('humidity'))['humidity__avg']
    
    # Determine if the weather is extreme
    extreme_conditions = 'Extreme' if data['temperature'] > 35 else 'Normal'
    
    context = {
        'weather': data,
        'avg_temp': avg_temp,
        'avg_humidity': avg_humidity,
        'alert': extreme_conditions
    }
    
    return render(request, 'alert.html', context)