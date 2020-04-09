from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from  listings.saerch_choices import all_cities,bedroom_choices,all_states,bathroom_choices,types_choices
def index(request):
    listings=Listing.objects.all().filter(is_published=True)[:3]
    context={
        'listings':listings,
        'all_cities':all_cities,
        'bedroom_choices':bedroom_choices,
        'all_states': all_states,
        'bathroom_choices':bathroom_choices,
        'types_choices': types_choices,
    }
    return render(request,'pages/index.html',context)

def aboutus(request):
    listings = Listing.objects.all()
    realtors = Realtor.objects.order_by('hire_date')
    context = {
        'listings': listings,
        'realtor':realtors,
    }
    return render(request,'pages/about-us.html',context)
