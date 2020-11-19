from django.db import models
from storeApp.models.instrument import Instrument
from storeApp.models.user import User


class Order(models.Model):

    id_instrument = models.ForeignKey(Instrument, on_delete=models.RESTRICT, db_column='id_instrument')
    id_user = models.ForeignKey(User, on_delete=models.RESTRICT, db_column='id_user')
