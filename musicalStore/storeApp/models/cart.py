from django.db import models
from .instrument import Instrument
from django.conf import settings


class Cart(models.Model):

    class Meta:
        db_table = 'cart'

    id_instrument = models.ForeignKey(Instrument, default=1, on_delete=models.RESTRICT, db_column='id_instrument')
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, db_column='id_user')
