# Generated by Django 2.1 on 2020-04-13 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_auto_20200412_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 13, 19, 24, 34, 45432)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='year_built',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 13, 19, 24, 34, 45432), null=True),
        ),
    ]
