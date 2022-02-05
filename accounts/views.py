from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import EditProfile, ProfileForm
from jsignature.utils import draw_signature


def register(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)

        if profile_form.is_valid():
            profile_form.save()

            messages.success(request, 'Your profile was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        profile_form = ProfileForm()
    return render(request, 'register.html', {
        'profile_form': profile_form,
    })


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout')


def edit_user(request):
    if request.method == 'POST':
        form = EditProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect('/edit_user')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = EditProfile(instance=request.user)
    return render(request, "edit_user.html", {'form':form })