from django.db import models
from storeApp.models.address import Address


class Provider(models.Model):

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=30)
    id_address = models.ForeignKey(Address, on_delete=models.RESTRICT, db_column='id_address')
