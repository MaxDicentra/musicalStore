from django.db import models
from .producer import Producer
from .provider import Provider
from .type import Type


class Instrument(models.Model):

    class Meta:
        db_table = 'instrument'

    name = models.CharField(max_length=45)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    id_type = models.ForeignKey(Type, on_delete=models.RESTRICT, db_column='id_type')
    id_producer = models.ForeignKey(Producer, on_delete=models.RESTRICT, db_column='id_producer')
    id_provider = models.ForeignKey(Provider, on_delete=models.RESTRICT, db_column='id_provider')
