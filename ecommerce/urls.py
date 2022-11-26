"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from ecommerce1.views import cate_view,view_brands,brands_delete,cate_delete,subcate_delete,subcate_view, payment_demo,order_payment, callback,view_product, delete_pro, ajax_get_states, ajax_call, ajax_get_data, index_page, edit_profile, category_page, logout_req, product_page, cart_page, checkout_page,login_page,register_page,subcategory_page,change_password, brands_pg,prod_master, remove_cart_prod
from management.views import add_slider, category_1, sub_category_1, brands_1, size_master_1,product_master_1,color_master_1
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page, name='home'),
    path('product/', product_page , name='product'),
    path('cart/',cart_page),
    path('checkout/', checkout_page),


    path('add_slider/', add_slider),
    path('add_category/', category_1),
    path('add_sub_category/', sub_category_1),
    path('size_master/', size_master_1),
    path('color_master/', color_master_1),
    path('product_master/', product_master_1),
    path('add_brands/', brands_1),
    
    
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_req),
    path('category/<int:id>', category_page),
    path('sub_category/<int:id>', subcategory_page),
    path('brands_pg/<int:id>', brands_pg),
    path('prod/<int:id>', prod_master),
    path('remove_prod/<int:id>', remove_cart_prod),

                # -----edit delete----

    path('edit_user/', edit_profile),
    path('change_password/',change_password),

                # -------ajax--------
    path('ajax_demo/',ajax_call),
    path('ajax_get_data/',ajax_get_data),
    path('ajax_get_states/',ajax_get_states),

    # -------------delete product - brands - category - sub category----------

    path('delete_pro/<int:id>',delete_pro),
    path('view_product/',view_product),

    path('cate_view/',cate_view),
    path('cate_delete/<int:id>',cate_delete),
    path('subcate_view/',subcate_view),
    path('subcate_delete/<int:id>',subcate_delete),
    path('view_brands/',view_brands),
    path('brands_delete/<int:id>',brands_delete),

    # ---------------razorpay-------------

    path("payment_demo/", payment_demo, name="payment_demo"),
    path("payment/", order_payment, name="payment"),
    path("callback/<int:id>", callback, name="callback"),
    


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)