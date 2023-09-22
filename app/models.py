from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
STATE_CHOICES=(
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andhra Pradesh','andhrapradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat	','Gujarat	'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh	','Madhya Pradesh	'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya	','Meghalaya	'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu	','Tamil Nadu	'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh	','Uttar Pradesh	'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal	','West Bengal	')
)
class Custemer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=200)
    locality= models.CharField(max_length=200)
    city= models.CharField(max_length=50)
    zipcode= models.IntegerField()
    state= models.CharField( choices=STATE_CHOICES, max_length=50)
    
    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)
class Product(models.Model):
    title= models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=100)
    Product_image=models.ImageField(upload_to='productimg')
    
    def __str__(self):
        return str(self.id)
    
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product=models.ForeignKey(User,on_delete=models.CASCADE)
#     quantity=models.PositiveIntegerField(default=1)
    
#     def __str__(self):
#         return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='carts_for_product')
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    
STATE_CHOICES=(
    ('Accepted','Accepted'),
    ('packed','packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

# class OrderPlaced(models.Model):
#     user= models.CharField(max_length=100)
#     # Custemer=models.ForeignKey(User, on_delete=models.CASCADE)
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     Product=models.ForeignKey(User, on_delete=models.CASCADE)
#     quanity=models.PositiveBigIntegerField(default=1)
#     Ordered_date=models.DateTimeField(auto_now_add=True)
#     status=models.CharField(max_length=50, status=STATE_CHOICES, default='pending')
    
class OrderPlaced(models.Model):
    user = models.CharField(max_length=100)  # This field needs a CharField or ForeignKey, not just CharField
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming Product is another model
    quantity = models.PositiveBigIntegerField(default=1)
    Ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATE_CHOICES, default='pending')