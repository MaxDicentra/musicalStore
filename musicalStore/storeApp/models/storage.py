from django.db import models
from .instrument import Instrument


class Storage(models.Model):

    class Meta:
        db_table = 'storage'

    id_instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT, db_column='id_instrument')
    amount = models.IntegerField(default=0)