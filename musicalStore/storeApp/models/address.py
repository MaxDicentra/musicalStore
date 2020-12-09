from django.db import models


class Address(models.Model):

    class CityType(models.enums.TextChoices):
        CIT = 'city'
        VIL = 'village'
        TOW = 'town'

    class StreetType(models.enums.TextChoices):
        STR = 'street'
        LAN = 'lane'
        AVN = 'avenue'

    class Meta:
        db_table = 'address'

    country = models.CharField(max_length=45, blank=True)
    city_type = models.CharField(max_length=10, choices=CityType.choices,blank=True)
    city = models.CharField(max_length=45, blank=True)
    street_type = models.CharField(max_length=10, choices=StreetType.choices, blank=True)
    street = models.CharField(max_length=45, blank=True)
    house = models.CharField(max_length=10, blank=True)
    gate = models.CharField(max_length=5, blank=True)
    flat = models.CharField(max_length=10, blank=True)
    index = models.CharField(max_length=10, blank=True)
