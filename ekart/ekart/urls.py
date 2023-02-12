"""ekart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ekartapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('adminpage',views.admin_page,name='adminpage'),
    path('mycart',views.my_cart,name='mycart'),
    path('register',views.register,name='register'),
    path('adminallproducts',views.admin_all_products,name='adminallproducts'),
    path('user_register',views.user_register,name='user_register'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('login_index',views.login_index,name='login_index'),
    path('add_product_page',views.add_product_page,name='add_product_page'),
    path('addproduct_handler',views.add_product,name='addproduct_handler'),
    path('edit_product_page/<int:product_id>',views.edit_product_page,name='edit_product_page'),
    path('edit_product_handler/<int:product_id>',views.edit_product_handler,name='edit_product_handler'),
    path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('profile',views.profile,name='profile'),
    path('edit_profile/<int:user_id>',views.edit_profile,name='edit_profile'),
    path('edit_profile_handler/<int:id>',views.edit_profile_handler,name='edit_profile_handler'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('address',views.address,name='address'),
    
    





]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
