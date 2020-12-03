from django.db import models
from django.conf import settings
from .address import Address


class UserConnection(models.Model):

    class Meta:
        db_table = 'user_connection'
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    confirmed = models.BooleanField(default=False)
    id_address = models.ForeignKey(Address, on_delete=models.RESTRICT, db_column='id_address')
