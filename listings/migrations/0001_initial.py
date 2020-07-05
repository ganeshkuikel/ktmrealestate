# Generated by Django 2.1 on 2020-07-05 06:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField(null=True)),
                ('bathrooms', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('garage', models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('total_rooms', models.IntegerField(blank=True, null=True)),
                ('sqft', models.IntegerField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('year_built', models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 5, 12, 24, 41, 893466), null=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 5, 12, 24, 41, 893466))),
                ('location', models.CharField(blank=True, max_length=400)),
                ('aerial_view', models.CharField(blank=True, max_length=400)),
                ('street_view', models.CharField(blank=True, max_length=400)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings.Listing')),
            ],
        ),
    ]
