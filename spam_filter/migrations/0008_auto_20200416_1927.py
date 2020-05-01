# Generated by Django 2.1 on 2020-04-16 13:42

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spam_filter', '0007_auto_20200416_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='spam_filtering',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 19, 26, 2, 655615), null=True),
        ),
    ]
