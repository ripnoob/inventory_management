from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, update_session_auth_hash
from .forms import AccountUpdateForm

@login_required
def UpdateAccountInfo(request):
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)

            current_password = form.cleaned_data.get('current_password')
            if current_password and not authenticate(username=user.username, password=current_password):
                messages.error(request, 'Invalid current password.')
                return redirect('dashboard:update_account')

            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)

            user.save()
            messages.success(request, 'Your account information was successfully updated.')
            return redirect('inventory:dashboard')
        else:
        	for field, errors in form.errors.items():
        		for error in errors:
        			messages.error(request, error)
    context = {'user':request.user}

    return render(request, 'dashboard/account_update.html', context)
