# Generated by Django 2.1 on 2020-08-06 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_filter', '0007_auto_20200806_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 12, 11, 8, 986658), null=True),
        ),
    ]
