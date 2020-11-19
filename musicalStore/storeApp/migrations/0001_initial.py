# Generated by Django 3.1.3 on 2020-11-19 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=45)),
                ('city_type', models.CharField(choices=[('city', 'Cit'), ('village', 'Vil'), ('town', 'Tow')], max_length=10)),
                ('city', models.CharField(max_length=45)),
                ('street_type', models.CharField(choices=[('street', 'Str'), ('lane', 'Lan'), ('avenue', 'Avn')], max_length=10)),
                ('street', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=10)),
                ('gate', models.CharField(max_length=5)),
                ('flat', models.CharField(max_length=10)),
                ('index', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=250)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=30)),
                ('id_address', models.ForeignKey(db_column='id_address', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=30)),
                ('id_address', models.ForeignKey(db_column='id_address', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=45)),
                ('inst', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.IntegerField()),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('user', 'User')], max_length=10)),
                ('id_address', models.ForeignKey(db_column='id_address', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.address')),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('description', models.TextField(max_length=250)),
                ('price', models.IntegerField()),
                ('id_producer', models.ForeignKey(db_column='id_producer', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.producer')),
                ('id_provider', models.ForeignKey(db_column='id_provider', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.provider')),
                ('id_type', models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.type')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_instrument', models.ForeignKey(db_column='id_instrument', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.instrument')),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.user')),
            ],
        ),
        migrations.AddField(
            model_name='instrument',
            name='id_producer',
            field=models.ForeignKey(db_column='id_producer', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.producer'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='id_provider',
            field=models.ForeignKey(db_column='id_provider', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.provider'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='id_type',
            field=models.ForeignKey(db_column='id_type', on_delete=django.db.models.deletion.RESTRICT, to='storeApp.type'),
        ),
    ]
