from django.db import models
from .instrument import Instrument
from .order import Order


class OrderedInstr(models.Model):

    class Meta:
        db_table = 'ordered_instr'

    id_instrument = models.ForeignKey(Instrument, default=1, on_delete=models.RESTRICT, db_column='id_instrument')
    id_order = models.ForeignKey(Order, on_delete=models.RESTRICT, db_column='id_order')
