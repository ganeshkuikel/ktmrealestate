from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
# Create your views here.
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

                        # Login after register
                        #     auth.login(request,user)
                        #     messages.success(request,'You are now logged in')
                        #     return redirect('index')
                        user.save()
                        messages.success(request,'You are registered and can log in now')
                        return redirect('index')

        else:
            messages.error(request,"Passwords do not match!! Please enter again")
            return redirect('register_page')
    else:
        return render(request,'pages/register_page.html')

def login(request):
    if request.method=='POST':
       username=request.POST['username']
       password=request.POST['password']

       user=auth.authenticate(username=username,password=password)
       if user is not None:
           auth.login(request,user)
           messages.success(request,'You are now logged in ')
           return redirect('dashboard')
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

def dashboard(request):
    return render(request,'pages/dashboard.html')