from django.db import models
from django.template.defaultfilters import slugify
from math import pow

class Asteroid(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    closest_date = models.DateField()
    closest_distance = models.FloatField()
    diameter = models.CharField(max_length=25)
    velocity = models.FloatField()
    next_to_earth = models.BooleanField()

    class Meta:
        app_label = 'stalker'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Asteroid, self).save(*args, **kwargs)