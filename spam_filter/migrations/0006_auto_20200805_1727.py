# Generated by Django 2.1 on 2020-08-05 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_filter', '0005_auto_20200805_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 17, 27, 42, 446168), null=True),
        ),
    ]
