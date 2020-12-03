from django.db import models
from .address import Address


class Producer(models.Model):

    class Meta:
        db_table = 'producer'

    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=30)
    id_address = models.ForeignKey(Address, on_delete=models.RESTRICT, db_column='id_address')
