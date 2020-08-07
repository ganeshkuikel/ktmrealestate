from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/account/login")
def contact(request):
    if request.method=='POST':
        if user.is_authenticated:
            listing_id = request.POST['listing_id']
            listing = request.POST['listing']
            name = request.user.first_name + " " + request.user.last_name
            email = request.user.email
            phone = request.POST['phone']
            message = request.POST['message']
            realtor_email = request.POST['realtor_email']


        # Check user inquiry made or not

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contacted:
                messages.error(request,"You have already made an enquiry for this listing")
                return redirect('/listings/' + listing_id)




        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        # Email Send

        # send_mail(
        #     'Property Listing Inquiry',
        #     'A new inquiry has been posted for ' + listing + ' Sign into the admin panel for more info',
        #     'ktmrealestate78@gmail.com',
        #     [realtor_email,'ganeshkuikel66@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request,"Your requests has been posted thank you for your response")
        return redirect('/listings/'+listing_id)
