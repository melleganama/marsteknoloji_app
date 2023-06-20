from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.core.validators import RegexValidator
from products.models import Product
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture     = ResizedImageField(default='profile_pics/default.png', size=[200, 200], upload_to='profile_pics')
    first_name          = models.CharField(max_length=50, blank=True)
    last_name           = models.CharField(max_length=50, blank=True)
    adress              = models.CharField(max_length=100, blank=True)
    
    phone_regex         = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '0(5xx) xxx xx xx'.")
    number              = models.CharField(validators=[phone_regex], max_length=11, blank=True)
   
   
   
    def __str__(self):
        return f"{self.user.username} Profile"



class Wishlist(Product):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    def __str__(self):
        return f"{self.user.username} Wishlist"
    
    
"""
class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='WishlistItem')
    
    def __str__(self):
        return f"{self.user.username} Wishlist"
    
class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

"""