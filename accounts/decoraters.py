from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied


def unauthenticated_user(view_func):

	def wrapper_func(request,*args,**kwargs):

		if request.user.is_authenticated:
			return redirect('index')
		else:

			return view_func(request,*args,**kwargs)

	return wrapper_func


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request,*args,**kwargs):
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in allowed_roles:
				return view_func(request,*args,**kwargs)
			else:
				raise PermissionDenied

		return wrapper_func
	return decorator


def admin_and_realtors(view_func):
	def wrapper_func(request,*args,**kwargs):
		group=None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('index')

		
		if group == 'admin' or group == 'realtor':
			return view_func(request,*args,**kwargs)
		else:
			raise PermissionDenied


	return wrapper_func

