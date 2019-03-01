from django.contrib import admin
from .models import Profile, ProfileProvider, ProfileSeeker
# Register your models here.

admin.site.register(Profile)
admin.site.register(ProfileProvider)
admin.site.register(ProfileSeeker)
