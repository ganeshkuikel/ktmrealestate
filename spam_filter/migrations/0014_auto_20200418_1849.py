# Generated by Django 2.1 on 2020-04-18 13:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_filter', '0013_auto_20200417_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 18, 47, 30, 987174), null=True),
        ),
    ]
