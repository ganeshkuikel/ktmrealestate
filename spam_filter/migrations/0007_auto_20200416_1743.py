# Generated by Django 2.1 on 2020-04-16 11:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_auto_20200416_1743'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spam_filter', '0006_remove_spam_filtering_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spam_filtering',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='spam_filtering',
            name='user_firstname',
        ),
        migrations.RemoveField(
            model_name='spam_filtering',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='spam_filtering',
            name='user_lastname',
        ),
        migrations.AddField(
            model_name='spam_filtering',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Listing'),
        ),
        migrations.AddField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 17, 42, 16, 589232), null=True),
        ),
        migrations.AddField(
            model_name='spam_filtering',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
