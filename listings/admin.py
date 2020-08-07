from django.contrib import admin

from .models import Listing,ListingImage,Confirm_Sales


class ListingImageAdmin(admin.StackedInline):
	model = ListingImage




@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
	list_display = ('id','title','is_published','price','list_date')   
    # list_display_links = ('id','title')   
    # list_filter = ('realtor','city','state')    
    # list_editable = ('is_published',)
    # search_fields = ('title','description','address','city','state','price','category')
    # list_per_page = 20
	inlines=[ListingImageAdmin]


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
	pass
@admin.register(Confirm_Sales)
class ConfirmedListing(admin.ModelAdmin):
	pass






