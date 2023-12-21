from django.db import models

class House(models.Model):
    bedrooms = models.IntegerField()
    location = models.CharField(max_length=100)
    square_footage = models.FloatField()
    price = models.FloatField(null=True, blank=True)
