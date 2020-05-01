from django.urls import  path
from django.conf.urls import url
from . import views

urlpatterns=[path('',views.index,name='listings'),
             path('<int:listing_id>',views.listing,name='listing'),
             path('search',views.search,name='search'),
             path('date_wise',views.date,name='date_wise'),
             path('low_to_high',views.low_to_high,name='low_to_high'),
             path('high_to_low',views.high_to_low,name='high_to_low'),
             path('list_view',views.list_view,name='list_view'),
             path('new_date_list',views.listview_newdate,name='new_date_list'),
             path('price_low',views.listview_pricelow,name='price_low'),
             path('price_high',views.listview_pricehigh,name='price_high'),
             url(r'^favourite_post/$',views.favourite_post,name='favourite_post'),
]