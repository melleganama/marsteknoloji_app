from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Wishlist

#from django_cleanup import cleanup
#from .models import Profile

# Create your views here.



@login_required
def wishlist(request):
    wishlists = Wishlist.objects.filter(user = request.user)
    return render(request, "users/wishlist.html", {'wishlists':wishlists})


"""
@login_required
def add_wishlist(request, id, *args):
    
    referring_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    
    whislist, _ = Wishlist.objects.get_or_create(user=request.user)
    wishlist_item, created = WishlistItem.objects.get_or_create(whislist=whislist, product=product)
    if not created:
        wishlist_item.quantity += 1
        wishlist_item.save()
    return redirect(referring_page)  # Redirect to the cart page

"""

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            
            form.save()
            
            messages.success(request, f"{username}, Your Account Has Been Created. Login Now!")
            
            return redirect("users:login")
    else:
        form = UserRegisterForm()
    
    return render(request, "users/register.html", {'form':form})


@login_required
def profile(request):
    """managing profile form"""
    if request.method == "POST":
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if p_form.is_valid():
                       
            # Clean up the previous profile picture
            #cleanup(instance=request.user.profile.profile_picture)
            
            p_form.save()
            messages.success(request, f"Your Profile Has Been Updated.")
            return redirect("users:profile")
            
    
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
        
        
    
    """managing user form"""
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        
        if u_form.is_valid():
                                  
            u_form.save()
            messages.success(request, f"Your Informations Has Been Updated.")
            return redirect("users:profile")
            
    
    else:
        u_form = UserUpdateForm(instance=request.user)
        
    context = {
        "p_form" : p_form,
        "u_form" : u_form,
    }
    
    
    return render(request, "users/profile.html", context)