# Generated by Django 3.1.3 on 2020-12-02 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userconnection',
            name='name',
        ),
        migrations.RemoveField(
            model_name='userconnection',
            name='surname',
        ),
    ]
