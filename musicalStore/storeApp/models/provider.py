from django.db import models
from .address import Address


class Provider(models.Model):

    class Meta:
        db_table = 'provider'

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=30)
    id_address = models.ForeignKey(Address, on_delete=models.RESTRICT, db_column='id_address')
