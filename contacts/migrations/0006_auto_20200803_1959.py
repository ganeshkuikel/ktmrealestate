# Generated by Django 2.1 on 2020-08-03 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20200705_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 19, 59, 2, 848248)),
        ),
    ]
