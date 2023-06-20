from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import AddProductsForm
from django.contrib import messages
from .models import Product
from django.contrib.auth.models import User
# Create your views here.



def products_list(request):
    products = Product.objects.all()
    keyword = request.GET.get("user_search")
    min_price_filter = request.GET.get('product-price-range')
    #max_price_filter = request.GET.get('max_price')
    category_filter = request.GET.get('product-category')
    
    categories = Product.objects.values_list('product_category', flat=True).distinct()
    
    
    if keyword:
        products = Product.objects.filter(product_name__contains=keyword)

    if min_price_filter:
        products = products.filter(product_price__lte=min_price_filter)

    if category_filter:
        products = products.filter(product_category__icontains=category_filter)
        
    context = {
            'products': products,
            'categories':categories,
        }

    return render(request, "products/products_list.html", context)




def product_detail(request, id):
    product = get_object_or_404(Product, id=id)    
    related_products = Product.objects.filter(product_category=product.product_category)
    
    
    context = {
        'related_products':related_products,
        'product':product,        
    }
    
    return render(request, "products/product_detail.html", context)







@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_store(request):                
    return render(request, "products/manage_store.html")


@login_required
@user_passes_test(lambda u: u.is_staff)
def add_product(request):
    
    """managing add product form"""
    
    if request.method == 'POST':
        add_form = AddProductsForm(request.POST, request.FILES)
        # request.FILES allow us to upload files like pictures.
        
        if add_form.is_valid():
            add_form.save()
            messages.success(request, "Product Added Successfully !")
            return redirect("products:add_product")           
    else:
        add_form = AddProductsForm()
        
        
        context = {
            'add_form' : add_form,
        }
            
                
        return render(request, "products/add_product.html", context)



@login_required
@user_passes_test(lambda u: u.is_staff)
def all_products(request):    
    """managing update product form"""
    keyword = request.GET.get("manager_search")
    
    if keyword:
        products = Product.objects.filter(product_name__icontains=keyword)
        
        return render(request, "products/all_products.html", {"products": products,})
    
    else:
        products = Product.objects.all()
        return render(request, "products/all_products.html", {"products": products,})
        


@login_required
@user_passes_test(lambda u: u.is_staff)
def update_product(request, id):  
    product =get_object_or_404(Product, id=id)  
    
    update_form = AddProductsForm(request.POST or None, request.FILES or None, instance=product)
    
    if update_form.is_valid():
        update_form.save()
        messages.success(request, "Product Updated")
        return redirect("products:all_products")
    
    else:
        return render(request, "products/update_product.html", {'update_form':update_form})
        

@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_product(request, id):  
    product = get_object_or_404(Product, id=id)  
    
    return render(request, "products/delete_product.html", {'product':product})



@login_required
@user_passes_test(lambda u: u.is_staff)
def verified_delete_product(request, id):  
    product = get_object_or_404(Product, id=id)  
    product.delete()
    
    messages.success(request, "Product Successfullly Deleted!")

    return redirect("products:all_products")


@login_required
@user_passes_test(lambda u: u.is_staff)
def manage_users(request):  
    
    keyword = request.GET.get("search_user")
    
    if keyword:
        users = User.objects.filter(username__icontains=keyword)
        
        return render(request, "products/manage_users.html", {"users": users})
    
    else:
        users = User.objects.all()
        return render(request, "products/manage_users.html", {"users": users})
        



@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_user(request, id):  
    users = get_object_or_404(User, id=id)  
    
    return render(request, "products/delete_user.html", {'users':users})



@login_required
@user_passes_test(lambda u: u.is_staff)
def verified_delete_user(request, id):  
    user = get_object_or_404(User, id=id)  
    user.delete()
    
    messages.success(request, "User Successfullly Deleted!")

    return redirect("products:manage_users")




