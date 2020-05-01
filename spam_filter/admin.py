from django.contrib import admin
from .models import Spam_filtering
from .views import accuracy

# Register your models here.

class SpamAdmin(admin.ModelAdmin):
    list_display = ('type','comments','user_id','listing')
    accuracy


admin.site.register(Spam_filtering,SpamAdmin)
