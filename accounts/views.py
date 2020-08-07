from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from listings.models import Listing
# Create your views here.
from requests import request
from accounts.decoraters import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
from django.http import HttpResponse


@unauthenticated_user
def register(request):

    if request.method=='POST':
        # Get values
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pass']
        r_password=request.POST['re_pass']

    #     Check if password match

        if password==r_password:

                    if User.objects.filter(username=username).exists():
                        messages.error(request,"The given username already exists")
                        return redirect('register_page')
                    else:
                        if User.objects.filter(email=email).exists():
                            messages.error(request, "The given email is being used")
                            return redirect('register_page')
                        else:
                            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)

                        user.save()

                        group = Group.objects.get(name='customer')
                        user.groups.add(group)

                        messages.success(request,'You are registered and can log in now')
                        return redirect('index')

        else:
            messages.error(request,"Passwords do not match!! Please enter again")
            return redirect('register_page')
    else:
        return render(request,'pages/register_page.html')

@unauthenticated_user
def login(request):
    
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']

       user=auth.authenticate(username=username,password=password)
       if user is not None:
            auth.login(request,user)
            group=None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group == 'customer':
                messages.success(request,'You are now logged in ')
                return redirect('dashboard')
            if group == 'admin' or 'realtor':
                return redirect('realtor_index')
       else:
           messages.error(request,'Invalid credentials')
           return redirect('login')
    else:
        return render(request,'pages/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        messages.success(request,'You are now logout successfully')
        return redirect('login')
    else:
        return HttpResponse("Not logged out")
@login_required
def dashboard(request):
    user=request.user
    favourite_posts = user.favorite.all()
    context = {
        'favourite_post':favourite_posts,
    }

    return render(request,'pages/dashboard.html',context)