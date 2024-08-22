from django.urls import path
from . import views

urlpatterns = [
    path('weather-update/', views.weather_update, name='weather_update'),
]