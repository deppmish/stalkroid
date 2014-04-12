from django.db import models

class Asteroid(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    closest_date = models.DateField()
    closest_distance = models.FloatField()
    absolute_magnitude = models.FloatField()
    diameter = models.FloatField()
    confidence = models.FloatField()