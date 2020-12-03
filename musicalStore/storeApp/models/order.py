from django.db import models
from .instrument import Instrument
from django.conf import settings


class Order(models.Model):

    class Meta:
        db_table = 'order'

    id_instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT, db_column='id_instrument')
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, db_column='id_user')
