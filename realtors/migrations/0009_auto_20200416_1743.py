# Generated by Django 2.1 on 2020-04-16 11:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0008_auto_20200415_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 16, 17, 42, 16, 535281)),
        ),
    ]
