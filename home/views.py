from django.shortcuts import render, redirect
from products.models import Product

# Create your views here.


def index(request): 
    featured_products = Product.objects.all()
    recent_products = Product.objects.all()
    keyword = request.GET.get("user_search")
         
    if keyword:
        products = Product.objects.filter(product_name__contains=keyword)
        return render(request, "products/products_list.html", {'products':products})
        
        
    context = {
        'featured_products' : featured_products,
        'recent_products' : recent_products,
    }
    return render(request, "home/index.html", context)


def contact(request):
    return render(request, "home/contact.html")