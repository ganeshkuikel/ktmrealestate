# Generated by Django 2.1 on 2020-08-06 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_filter', '0006_auto_20200805_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 11, 41, 4, 592107), null=True),
        ),
    ]
