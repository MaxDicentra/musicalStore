from django.db import models
from storeApp.models.address import Address


class User(models.Model):

    class Roles(models.enums.TextChoices):
        ADMIN = 'admin'
        USER = 'user'

    name = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    password = models.IntegerField()
    role = models.CharField(max_length=10, choices=Roles.choices)
    id_address = models.ForeignKey(Address, on_delete=models.RESTRICT, db_column='id_address')
