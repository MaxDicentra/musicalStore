from django.db import models
from storeApp.models.producer import Producer
from storeApp.models.provider import Provider
from storeApp.models.type import Type


class Storage(models.Model):

    name = models.CharField(max_length=45)
    description = models.TextField(max_length=250)
    price = models.IntegerField()
    id_type = models.ForeignKey(Type, on_delete=models.RESTRICT, db_column='id_type')
    id_producer = models.ForeignKey(Producer, on_delete=models.RESTRICT, db_column='id_producer')
    id_provider = models.ForeignKey(Provider, on_delete=models.RESTRICT, db_column='id_provider')
