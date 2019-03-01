from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile, ProfileProvider, ProfileSeeker
from django.db import models


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # Default () is required=True. Could have (required=False) if email is not required.

    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # Default () is required=True. Could have (required=False) if email is not required.

    class Meta: 
        model = User
        fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']

class RoleSeekerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['service_seeker']

class RoleProviderForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['service_provider']


class ProfileUpdateForm_Provider(forms.ModelForm):
    class Meta:
        model = ProfileProvider
        fields = ['company_name', 'company_address', 'website', 'services_description']


class ProfileUpdateForm_Seeker(forms.ModelForm):
    class Meta:
        model = ProfileSeeker
        fields = ['first_name', 'last_name', 'street_name', 'zip_code', 'phone']

