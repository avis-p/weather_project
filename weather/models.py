from django.db import models
from django.utils import timezone

class WeatherData(models.Model):
    city = models.CharField(max_length=100, null=True)
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    timestamp = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        ordering = ['-timestamp']