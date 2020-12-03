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

    country = models.CharField(max_length=45)
    city_type = models.CharField(max_length=10, choices=CityType.choices)
    city = models.CharField(max_length=45)
    street_type = models.CharField(max_length=10, choices=StreetType.choices)
    street = models.CharField(max_length=45)
    house = models.CharField(max_length=10)
    gate = models.CharField(max_length=5)
    flat = models.CharField(max_length=10)
    index = models.CharField(max_length=10)
