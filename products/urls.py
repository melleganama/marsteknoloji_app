from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path('manage_store/', views.manage_store, name="manage_store"),
    path('add_product/', views.add_product, name="add_product"),
    path('all_products/', views.all_products, name="all_products"),
    path('update_product/<int:id>', views.update_product, name="update_product"),
    path('delete_product/<int:id>', views.delete_product, name="delete_product"), 
    path('verified_delete_product/<int:id>', views.verified_delete_product, name="verified_delete_product"), 
    path('all_products/', views.all_products, name="all_products"),
    path('manage_users/', views.manage_users, name="manage_users"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"), 
    path('verified_delete_user/<int:id>', views.verified_delete_user, name="verified_delete_user"), 
    path('product_detail/<int:id>', views.product_detail, name="product_detail"),    
    path('products_list/', views.products_list, name="products_list"),
]
