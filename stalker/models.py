from django.db import models
from django.template.defaultfilters import slugify
from math import pow

class Asteroid(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    closest_date = models.DateField()
    closest_distance = models.FloatField()
    absolute_magnitude = models.FloatField()
    diameter = models.FloatField()
    uncertainity = models.FloatField()
    confidence = models.FloatField()

    def get_confidence(self, uncertainity):
        confidence = 100 - (uncertainity * 10)

        return confidence

    def get_diameter(self, absolute_magnitude):
        """ This function has been created using this formula taken from  Stephen F. Austin University and using an asteroid albedo
        of 0.15 as default. 

        http://www.physics.sfasu.edu/astro/asteroids/sizemagnitude.html

        """

        diameter = 3432.334 * pow(10, -0.2*absolute_magnitude)

        return diameter

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        self.confidence = self.get_confidence(self.uncertainity)
        self.diameter = self.get_diameter(self.absolute_magnitude)
        
        super(Asteroid, self).save(*args, **kwargs)