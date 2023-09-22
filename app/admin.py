from django.contrib import admin
from.models import (
    Custemer,
    Product,
    Cart,
    OrderPlaced
)

# Register your models here.
@admin.register(Custemer)
class CustemerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','locality','city','zipcode','state']
    
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discount_price','brand','category','Product_image']
    
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['user', 'product', 'quantity']
    
    
@admin.register(OrderPlaced)   
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ('user', 'customer', 'Product', 'quantity', 'Ordered_date', 'status')

    