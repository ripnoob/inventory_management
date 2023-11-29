from django.http import HttpResponse, JsonResponse
from django.contrib import  messages
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			role = request.user.role
			if role in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				messages.warning(request, 'You do not have admin permission to perform this action.')
				return redirect(request.META.get('HTTP_REFERER', '/'))
		return wrapper_func
	return decorator


# def update_access(allowed_id[]):
# 	def decorator(view_func):
# 		def wrapper_func(request, *args, **kwargs):
# 			user_id = request.user.id
# 			if user_id in 