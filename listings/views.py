from django.shortcuts import render,get_object_or_404,get_list_or_404,HttpResponseRedirect,redirect
from pip._vendor.distro import like

from .models import Listing,ListingImage
from django.db import connection
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from  .saerch_choices import all_cities,bedroom_choices,all_states,bathroom_choices,types_choices
from spam_filter.models import Spam_filtering
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME







# Main listing page
def index(request):
    listings = Listing.objects.all()
    photos=ListingImage.objects.filter(photo__in=listings)
    paginator = Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'photos':photos,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
        # 'is_saved':is_saved,


    }
    return render(request,'listings/listings.html',context)

# Grid view search
def date(request):
    newest=Listing.objects.order_by('-list_date')
    paginator = Paginator(newest, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'date_listing': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/listing_date.html', context)

def low_to_high(request):
    low_to_high_price=Listing.objects.order_by('price')
    paginator = Paginator(low_to_high_price, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'low_to_high_price': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/low_to_high_listing_price.html', context)

def high_to_low(request):
    high_to_low_price=Listing.objects.order_by('-price')
    paginator = Paginator(high_to_low_price, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
         'high_to_low': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/high_to_low_price.html', context)

# List view sorting functions
def list_view(request):
    listings = Listing.objects.all()
    
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # Sort on new date in listview
    context = {
        # 'listings': paged_listings,
        'listings': paged_listings,
        
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,

    }
    return render(request, 'listings/listview.html', context)

def listview_newdate(request):
    newest=Listing.objects.order_by('-list_date')
    paginator = Paginator(newest, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'date_listing': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/listview/newdata_listview.html', context)

def listview_pricelow(request):
    low_to_high_price=Listing.objects.order_by('price')
    paginator = Paginator(low_to_high_price, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'low_to_high_price': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/listview/pricelow_listview.html', context)

def listview_pricehigh(request):
    high_to_low_price=Listing.objects.order_by('-price')
    paginator = Paginator(high_to_low_price, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'high_to_low': paged_listings,
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request, 'listings/listview/pricehigh_listview.html', context)

default_message = "You need to login first in order to continue"

@login_required(login_url="/account/login")
def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    photos=ListingImage.objects.filter(photo=listing)
    # is_liked=False
    # comment=CommentLikes.objects.get(pk=listing_id)
    # if comment.likes.filter(id=request.user.id).exists():
    #     is_liked=True
    id=request.POST.get('user_id')
    print(id)
    is_favourite=False
    if listing.favorite.filter(id=request.user.id).exists():
        is_favourite=True
    comments=Spam_filtering.objects.filter(listing=listing,type='ham').order_by('-id')



    context = {
        'listing':listing,
        'comments':comments,
        # 'is_liked':is_liked,
        # 'total_likes':comment.total_likes(),
        'is_favourite':is_favourite,
        'photos':photos,
    }

    return render(request,'listings/listing.html',context)






def search(request):

    query_list = Listing.objects.order_by('-list_date')

    # Types
    if 'categories' in request.GET:
        types_ap = request.GET['categories']
        if types_ap:
            query_list = query_list.filter(category__iexact=types_ap)

    # Keywords

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(description__icontains=keywords)

        # City
    if 'city' in request.GET:
        cities = request.GET['city']
        if cities:
            query_list = query_list.filter(city__iexact=cities)

        #    Districts

    if 'district' in request.GET:
        districts = request.GET['district']
        if districts:
            query_list = query_list.filter(district__iexact=districts)

        #  States
    if 'state' in request.GET:
        states = request.GET['state']
        if states:
            query_list = query_list.filter(state__iexact=states)

        #  Bedrooms

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_list = query_list.filter(bedrooms__lte=bedrooms)

        #  Prices
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)

        #        Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            query_list = query_list.filter(bathrooms__lte=bathrooms)



    if 'status' in request.GET:
        status = request.GET['status']
        if status:
            query_list = query_list.filter(status__iexact=status)

    if 'cities' in request.GET:
        cities = request.GET['cities']
        if cities:
            query_list = query_list.filter(city__iexact=cities)



    context = {
        'all_cities': all_cities,
        'bedroom_choices': bedroom_choices,
        'listings': query_list,
        'values': request.GET,
        'all_states': all_states,
        'bathroom_choices': bathroom_choices,
        'types_choices':types_choices,
    }

    return render(request, 'pages/search.html', context)

def favourite_post(request):
    listing = get_object_or_404(Listing,id=request.POST.get('listing_id'))
    is_liked=False
    if listing.favorite.filter(id=request.user.id).exists():
        listing.favorite.remove(request.user)
        is_liked=False
    else:
        listing.favorite.add(request.user)
        is_liked=True

    return HttpResponseRedirect(listing.get_absolute_url())








