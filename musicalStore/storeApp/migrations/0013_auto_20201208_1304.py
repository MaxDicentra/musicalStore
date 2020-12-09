# Generated by Django 3.1.3 on 2020-12-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0012_instrument_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='address',
            name='city_type',
            field=models.CharField(blank=True, choices=[('city', 'Cit'), ('village', 'Vil'), ('town', 'Tow')], max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='gate',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='address',
            name='house',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='index',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='address',
            name='street_type',
            field=models.CharField(blank=True, choices=[('street', 'Str'), ('lane', 'Lan'), ('avenue', 'Avn')], max_length=10),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='description',
            field=models.TextField(max_length=550),
        ),
    ]