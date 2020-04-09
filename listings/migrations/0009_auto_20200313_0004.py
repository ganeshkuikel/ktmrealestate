# Generated by Django 2.1 on 2020-03-12 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200309_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='aerial_view',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AddField(
            model_name='listing',
            name='street_view',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 13, 0, 4, 13, 824902)),
        ),
        migrations.AlterField(
            model_name='listing',
            name='year_built',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 13, 0, 4, 13, 824902), null=True),
        ),
    ]
