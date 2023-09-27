from django.urls import path
from app import views
from .views import ProductView, ProductDetailView  # Import ProductDetailView

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    path('', ProductView.as_view(), name='product-view'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),  # Use as_view() here
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    # path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm), name='passwordchange'),

    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm), name='passwordchange'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('mobile/<slug:data>/', views.mobile, name='mobile'),
    path('laptop/<slug:data>/', views.laptop, name='laptop'),
    path('topwear/<slug:data>/', views.topwear, name='topwear'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),    
    path('checkout/', views.checkout, name='checkout'),
    path('registration/', views.CustemerRegistrationView.as_view(), name='customerregistration'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
