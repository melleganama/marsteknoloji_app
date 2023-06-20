from django import forms
from .models import Product


class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_price', 'product_discount_price', 'stock_quantity', 'product_desc', 'product_specif', 'product_price', 'product_color', 'product_category', 'product_pic_1', 'product_pic_2', 'product_pic_3', 'product_pic_4']
        
        
  