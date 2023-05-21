# userprofile/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    print("Profile photo URL:", user_profile.profile_photo.url)  
    return render(request, 'userprofile/profile.html', {'user_profile': user_profile})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'userprofile/edit_profile.html', {'form': form})