# Generated by Django 2.0.6 on 2019-06-27 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivoryApp', '0006_tshirt_ts_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tshirt',
            name='ts_size',
        ),
    ]