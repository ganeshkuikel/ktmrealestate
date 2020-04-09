all_cities={
    'ktm' : 'kathmandu',
    'jhapa' : 'jhapa',
    'bhaktapur' :'bhaktapur',
    'lalitpur':'lalitpur',
    'butwal': 'butwal',
    'pokara': 'pokhara',
    'bhairawa':'bhairawa',
    'kawasoti':'kawasoti',
}

bedroom_choices={
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6+',
}
bathroom_choices={
    '1.0':'1',
    '2.0':'2',
    '3.0':'3',
    '4.0':'4',
    '5.0':'5',
    '6.0':'6+',
}

types_choices={
    'Apartment':'Apartment',
    'House':'House',
    'Land':'Land',
}

all_states={
    '1':'Province No.1',
    '2':'Province No. 2',
    '3':'Bagmati Pradesh',
    '4':'Gandaki Pradesh',
    '5':'Province No. 5',
    '6':'Karnali Pradesh',
    '7':'Sudurpashchim Pradesh',
    }

#     # City
#  if 'city' in request.GET:
#      cities = request.GET['city']
#      if cities:
#           query_list = query_list.filter(city__iexact=cities)
#
#     #    Districts
#
#  if 'district' in request.GET:
#         districts = request.GET['district']
#         if districts:
#             query_list = query_list.filter(district__iexact=districts)
#
# #  States
#  if 'state' in request.GET:
#         states = request.GET['state']
#         if states:
#             query_list = query_list.filter(state__iexact=states)
#
# #  Bedrooms
#
#  if 'bedrooms' in request.GET:
#         bedrooms = request.GET['bedrooms']
#         if bedrooms:
#             query_list = query_list.filter(bedrooms__lte=bedrooms)
#
#       #  Prices
#  if 'price' in request.GET:
#         price = request.GET['price']
#         if price:
#             query_list = query_list.filter(price__lte=price)
#
#      #        Bathrooms
#  if 'bathrooms' in request.GET:
#         bathrooms = request.GET['bathrooms']
#         if bathrooms:
#             query_list = query_list.filter(bathrooms__lte=bathrooms)
#
# # Types
#  if 'types' in request.GET:
#         types = request.GET['types']
#         if types:
#             query_list = query_list.filter(category__iexact=types)