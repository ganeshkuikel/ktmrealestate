from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','user','email','hire_date','is_mvp')
    list_display_links = ('id','user')
    search_fields = ('user',)
    list_editable = ('is_mvp',)
    list_per_page = 20
admin.site.register(Realtor,RealtorAdmin)
