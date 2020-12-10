from django.db import models

# Create your models here.
class FireData(models.Model):
    fire_weather_index = models.CharField(max_length=5)
    date = models.TextField()
