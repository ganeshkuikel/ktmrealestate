from django.db import models
from datetime import datetime
from realtors.models import Realtor
from django.db.models import Count
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone



class Listing(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=150)
    address=models.CharField(max_length=150,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    district=models.CharField(max_length=100,null=True)
    description=models.TextField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField(null=True)
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1,blank=True,null=True)
    garage = models.DecimalField(max_digits=2,decimal_places=1,null=True,blank=True)
    category = models.CharField( max_length=100,null=True, blank=True)
    total_rooms = models.IntegerField(blank=True,null=True)
    sqft=models.IntegerField(null=True,blank=True)
    is_published=models.BooleanField(default=True)
    favorite = models.ManyToManyField(User,related_name='favorite',blank=True)
    status = models.CharField(max_length=50,blank=True,null=True)
    year_built = models.DateTimeField(default=datetime.now(),blank=True,null=True)
    list_date=models.DateTimeField(default=datetime.now(),blank=True)
    location=models.CharField(max_length=400,blank=True)
    aerial_view = models.CharField(max_length=400, blank=True)
    street_view = models.CharField(max_length=400, blank=True)

    # Send Email to all users that are registered that admin has published a new listing.
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.title:
            subject="A new listings has been added by KTMRealEstate named: "+self.title
            message="Description: "+self.description 
            recievers = []
            recievers = User.objects.values_list('email', flat=True)
            print(recievers)
            # send_mail(subject,message,'ktmrealestate78@gmail.com',recievers,fail_silently = False)
            print("sent")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/listings/%s" %(self.id)

    def fav_counts(self):
        return self.favorite.count()

    def first_image(self):
         return self.images.first()


class ListingImage(models.Model):
    photo = models.ForeignKey(Listing,default=None,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return self.photo.title


    






