from django.db import models
from  datetime import datetime
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from listings.models import Listing


class Contact(models.Model):
    listing = models.ForeignKey(Listing,on_delete=models.SET_NULL, max_length=200,null=True)
    # listing_id=models.IntegerField(null=True)
    # name = models.CharField(max_length=100)
    # email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.CharField(blank=True,max_length=500)
    contact_date = models.DateTimeField(default=datetime.now(),blank=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name
