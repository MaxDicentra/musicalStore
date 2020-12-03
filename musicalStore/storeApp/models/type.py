from django.db import models


class Type(models.Model):

    class Meta:
        db_table = 'type'

    inst_type = models.CharField(max_length=45)
