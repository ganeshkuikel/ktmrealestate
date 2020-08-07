from django.urls import  path
from django.conf.urls import url
from realtors.views import *

urlpatterns = [
path('',index_realtor,name='realtor_index'),
path('contact_list',contact_inquiry,name='contact_list'),
url(r'^contact/data/$',ListContactCount.as_view(),name='contact_data')
]