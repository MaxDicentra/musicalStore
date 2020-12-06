from django.db import models
from .instrument import Instrument
from django.conf import settings
from django.contrib.auth.models import User


class Cart(models.Model):

    class Meta:
        db_table = 'cart'

    id_instrument = models.ForeignKey(Instrument, default=1, on_delete=models.RESTRICT, db_column='id_instrument')
    id_user = models.ForeignKey(User, default=1, on_delete=models.RESTRICT, db_column='id_user')
