# Generated by Django 2.1 on 2020-04-14 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0005_auto_20200413_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 14, 18, 33, 12, 545657)),
        ),
    ]
