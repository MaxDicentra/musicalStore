from django.db import models


class Type(models.Model):

    type = models.CharField(max_length=45)
    inst = models.CharField(max_length=10)
