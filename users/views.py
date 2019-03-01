from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import (UserRegisterForm, 
                    UserUpdateForm, 
                    ProfileUpdateForm, 
                    ProfileUpdateForm_Provider, 
                    ProfileUpdateForm_Seeker,
                    RoleSeekerForm,
                    RoleProviderForm
                    
                    )
from .models import Profile
# from django.views.generic import (ListView, DetailView, CreateView, UpdateView)
# from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
   
    return render(request,'users/register.html', {'form': form})


@login_required
def profile(request):  
    role = Profile.objects.filter(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, 
                                   instance=request.user.profile)
        role_seeker_form = RoleSeekerForm(request.POST, instance=request.user.profile)
        role_provider_form = RoleProviderForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            role_seeker_form.save()
            role_provider_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        role_seeker_form = RoleSeekerForm(instance=request.user.profile)
        role_provider_form = RoleProviderForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form': p_form,
        'role_seeker_form' : role_seeker_form,
        'role_provider_form' : role_provider_form,
        'role' : role
       
    }
    return render(request, 'users/profile.html', context)


@login_required
def profile_for_provider(request):
    if request.method == 'POST':
        provider_form = ProfileUpdateForm_Provider(request.POST, 
                                   instance=request.user.profileprovider)
       
        if provider_form.is_valid():
            provider_form.save()
            messages.success(request, f'Your Provider-profile has been updated!')
            return redirect('profile')
    else:
        provider_form = ProfileUpdateForm_Provider(instance=request.user.profileprovider)
   

    context = {
        
        'provider_form': provider_form
       
    }
    return render(request, 'users/provider_profile.html', context)


@login_required
def profile_for_seeker(request):
    if request.method == 'POST':
        seeker_form = ProfileUpdateForm_Seeker(request.POST, 
                                   instance=request.user.profileseeker)
       
        if seeker_form.is_valid():
            seeker_form.save()
            messages.success(request, f'Your Service Seeker Profile has been updated!')
            return redirect('profile')
    else:
        seeker_form = ProfileUpdateForm_Seeker(instance=request.user.profileseeker)
   

    context = {
        
        'seeker_form': seeker_form
       
    }
    return render(request, 'users/seeker_profile.html', context)


