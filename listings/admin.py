from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')    #Display the details of house in admin area
    list_display_links = ('id','title')   #Links from where we can go to detail of every house
    list_filter = ('realtor','city','state')    # list from where house can be filter using realtor wise
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','price','category')
    list_per_page = 20

admin.site.register(Listing,ListingAdmin)

