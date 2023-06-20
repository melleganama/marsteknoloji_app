from django.db import models
from django_resized import ResizedImageField
from django.core.exceptions import ValidationError

# Create your models here.


class CustomResizedImageField(ResizedImageField):
    """validates picture before saving to the database."""
    def validate(self, value, *args):
        super().validate(value, *args)
        
        # Add your custom validation logic here
        if hasattr(value.file, 'content_type') and value.file.content_type not in ['image/jpeg', 'image/png', 'image/jpg']:
            raise ValidationError('Only JPEG, JPG and PNG files are allowed.')


class Product(models.Model):
    
    COLOR_CHOICES = [
        ('Black' , 'Black'),
        ('Blue' , 'Blue'),
        ('Pink' , 'Pink'),
        ('Silver' , 'Silver'),
        ('white' , 'white'),
        ('Green' , 'Green'),
        ('Yellow' , 'Yellow'),
        ('transparent' , 'transparent')        
    ]
    
    CATEROGY_CHOICES = [
        ('computer' , 'computer'),
        ('phone' , 'phone'),
        ('keyboard' , 'keyboard'),
        ('mouse' , 'mouse'),
        ('earphones' , 'earphones'),
        ('phone cover' , 'phone cover'),
        ('computer components' , 'computer components')       
    ]
    
    
    product_name  = models.CharField(max_length=100)
    product_price  = models.PositiveIntegerField()    
    product_discount_price  = models.PositiveIntegerField(blank=True)
    stock_quantity  = models.PositiveIntegerField()
    product_desc  = models.TextField()
    product_specif  = models.TextField()
    product_color  = models.CharField(max_length=20, choices=COLOR_CHOICES)
    product_category  = models.CharField(max_length=20, choices=CATEROGY_CHOICES)
    product_pic_1      = CustomResizedImageField(size=[200, 200], upload_to='product_pics')
    product_pic_2      = CustomResizedImageField(size=[200, 200], upload_to='product_pics', blank=True)
    product_pic_3      = CustomResizedImageField(size=[200, 200], upload_to='product_pics', blank=True)
    product_pic_4      = CustomResizedImageField(size=[200, 200], upload_to='product_pics', blank=True)
     
    def __str__(self):
        return self.product_name
    