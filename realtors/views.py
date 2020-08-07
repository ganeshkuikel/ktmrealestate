from django.shortcuts import render
from accounts.decoraters import allowed_users,admin_and_realtors
from django.contrib.auth.decorators import login_required
from realtors.models import Realtor
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractMonth
from contacts.models import Contact


# Create your views here.

User = get_user_model()

@login_required(login_url="/account/login")
# @allowed_users(allowed_roles=['realtor'])
@admin_and_realtors
def index_realtor(request):
	realtor = Realtor.objects.all()
	context = {
	'realtors':realtor,
	}
	return render(request,'realtors/realtor.html')

@login_required(login_url="/account/login")
@admin_and_realtors
# @allowed_users(allowed_roles=['realtor'])
def contact_inquiry(request):
	return render(request,'realtors/contact_inquiry.html')


class ListContactCount(APIView):
	authentication_classes=[]
	permission_classes=[]
	def get(self,request,format=None):
		queryset = Contact.objects.annotate(month=TruncMonth(('contact_date'))).values_list('month', flat=True)
		month_totals = [ 0,0,0,0, 0,0,0,0, 0,0,0,0 ]
		for month in queryset:
			month=month.month-1
			month_totals[month] += 1
		labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
		result=[]
		for total in month_totals:
			result.append(total)
		data={
		'labels':labels,
		'default':result,
		}
		print(result)
		return Response(data)
		



count = Contact.objects.annotate(month=TruncMonth(('contact_date'))).values_list('month', flat=True)

print(count)
# Get contacts counts
# from django.db.models import Count
# from django.db.models.functions import TruncMonth
# from contacts.models import Contact
# Contact.objects.annotate(month=TruncMonth('contact_date')).values('month').annotate(total=Count('id'))
