# Generated by Django 2.1 on 2020-08-03 14:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtors', '0002_auto_20200705_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realtor',
            name='name',
        ),
        migrations.AddField(
            model_name='realtor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_realtor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 3, 19, 59, 2, 839307)),
        ),
    ]
