from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):    
    
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '0(5xx) xxx xx xx'.")    
    
    last_name       = forms.CharField(label="Last Name", max_length=20 , required=False)
    #number          = forms.CharField(validators=[phone_regex], label="Phone Number", max_length=11, min_length=11, widget=forms.TextInput(attrs={'placeholder': '0(5xx) xxx xx xx'}))
    email           = forms.EmailField()
    #adress          = forms.CharField(label="Full Adress", max_length=100)

    
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']
    
    
class UserUpdateForm(forms.ModelForm):
    email           = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']
    
    
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'profile_picture', 'adress', 'number']
        


"""    
class WishlistForm(forms.ModelForm):
    
    class Meta:
        model = Wishlist
        fields = ['quantity','product_name', 'product_price', 'product_discount_price'] 
        
"""  