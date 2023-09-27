from django.shortcuts import render
from django.views import View
from .models import Product
from.forms import CustemerRegistrationForm
from django.contrib import messages

class ProductView(View):
    def get(self, request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        mobiles = Product.objects.filter(category='M')

        return render(request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles})

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

def add_to_cart(request):
    return render(request, 'app/addtocart.html')

def buy_now(request):
    return render(request, 'app/buynow.html')

def profile(request):
    return render(request, 'app/profile.html')

def address(request):
    return render(request, 'app/address.html')

def orders(request):
    return render(request, 'app/orders.html')

# def change_password(request):
#     return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data== 'all':
        mobiles = Product.objects.filter(category='M')      
    elif data == 'Redmi' or data == 'Samsung':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'above':
        mobiles = Product.objects.filter(category='M').filter(discount_price__gte=10000)
    elif data == 'below':
        mobiles = Product.objects.filter(category='M').filter(discount_price__lt=10000)

    return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data=None):
    if data== 'all':
        laptops = Product.objects.filter(category='L')      
    elif data == 'hp' or data == 'lenovo' or data=='dell' or data=='asus':
        laptops = Product.objects.filter(category='L').filter(brand=data)
    elif data == 'above':
        laptops = Product.objects.filter(category='L').filter(discount_price__gte=60000)
    elif data == 'below':
        laptops = Product.objects.filter(category='L').filter(discount_price__lt=60000)

    return render(request, 'app/laptop.html', {'laptops': laptops})

def topwear(request, data=None):
    topwears = Product.objects.none()  # Initialize with an empty queryset

    if data == 'all':
        topwears = Product.objects.filter(category='M')      
    elif data == 'zara' or data == 'raymond':
        topwears = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'above':
        topwears = Product.objects.filter(category='M').filter(discount_price__gte=200)
    elif data == 'below':
        topwears = Product.objects.filter(category='M').filter(discount_price__lt=200)

    return render(request, 'app/topwear.html', {'topwears': topwears})

# def login(request):
#     return render(request, 'app/login.html')

# def customerregistration(request):
#     return render(request, 'app/customerregistration.html')

class CustemerRegistrationView(View):
    def get(self,request):
        form=CustemerRegistrationForm ()
        return render(request, 'app/customerregistration.html',{'form':form})
    
    def post(self,request):
        form=CustemerRegistrationForm (request.POST)  
        if form.is_valid():
            messages.success(request, 'congratulations!! registration successfull')
            form.save()
        return render(request, 'app/customerregistration.html',{'form':form})

def checkout(request):
    return render(request, 'app/checkout.html')
