# Generated by Django 2.1 on 2020-06-03 10:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 3, 10, 4, 44, 673716, tzinfo=utc)),
        ),
    ]
