# Generated by Django 2.1 on 2020-04-17 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_filter', '0011_auto_20200416_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 17, 6, 55, 4, 316101), null=True),
        ),
    ]
