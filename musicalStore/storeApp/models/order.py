from django.db import models
from django.conf import settings
from datetime import datetime
from .user_connection import UserConnection


class Order(models.Model):

    class Meta:
        db_table = 'order'

    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, db_column='id_user')
    id_user_info = models.ForeignKey(UserConnection, default=1, on_delete=models.RESTRICT)
    date = models.DateField(default=datetime.now, blank=True)
