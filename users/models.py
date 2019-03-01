from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
# from .current_user import get_current_user
# from django.urls import reverse
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    service_seeker = models.BooleanField(default=True)
    service_provider = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username} Profile'

class ProfileProvider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    service_seeker_check = models.ForeignKey(Profile,default=True, on_delete=models.CASCADE)
    company_name = models.CharField(default='',blank=True, max_length=30)
    company_address = models.CharField(default='',blank=True,max_length=30)
    website = models.CharField(default='',blank=True,max_length=30)
    services_description = models.TextField(default='',blank=True)
    def __str__(self):
        return f'{self.user.username} Profile for Provider'


class ProfileSeeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(default='',blank=True, max_length=30)
    last_name = models.CharField(default='',blank=True,max_length=30)
    street_name = models.CharField(default='',blank=True,max_length=30)
    zip_code = models.IntegerField(default=0000,blank=True)
    phone = models.CharField(default='', blank=True,max_length=13)
    def __str__(self):
        return f'{self.user.username} Profile for Seeker'

