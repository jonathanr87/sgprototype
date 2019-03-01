from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, ProfileProvider, ProfileSeeker


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


# @receiver(post_save, sender=User)
# def save_profileseeker(sender, instance, **kwargs):
#     instance.profileseeker.save()

# @receiver(post_save, sender=User)
# def save_profileprovider(sender, instance, **kwargs):
#     instance.profileprovider.save()

@receiver(post_save, sender=User)
def create_profileprovider(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return(ProfileProvider.objects.get_or_create(user=instance))
        post_save.connect(create_profileprovider, sender=User)
        
@receiver(post_save, sender=User)
def create_profileseeker(sender, instance, created, *args, **kwargs):
    # ignore if this is an existing User
    if not created:
        return(ProfileSeeker.objects.get_or_create(user=instance))
        post_save.connect(create_profileseeker, sender=User)

