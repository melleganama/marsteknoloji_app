from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Wishlist



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """ create a profile each time a new user is created """
    if created:
        Profile.objects.create(user=instance)
        
        
        

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """ save a profile each time a user is saved """
    instance.profile.save()
    
""" 
@receiver(post_save, sender=User)
def create_wishlist(sender, instance, created, **kwargs):
    #create a wishlist each time a new user is created
    if created:
        Wishlist.objects.create(user=instance)
        
        
        

@receiver(post_save, sender=User)
def save_wishlist(sender, instance, **kwargs):
    #save a wishlist each time a user is saved 
    instance.wishlist.save()
    
    
"""  