
from turtle import title
from django.shortcuts import render
from django.shortcuts import render,redirect
from ecommerce1.models import states,Country,Order
from management.models import Sliders, brands,category,chackout_register, new_register,product_master,size_master,add_to_cart,color_master, sub_category,chackout_register
from django.views.decorators.csrf import csrf_exempt
import razorpay
from ecommerce.settings import (
    RAZORPAY_KEY_ID,
    RAZORPAY_KEY_SECRET,
)
from .constants import PaymentStatus
from django.views.decorators.csrf import csrf_exempt
import json 

# Create your views here.
def index_page(request):
    if 'xyz' in request.session:
        user_id = request.session['xyz']
        user = new_register.objects.filter(id=user_id).get()
        cart_product = add_to_cart.objects.filter(user_id=user_id).all()
    else:
        user_id = ''
        cart_product = ''
        user=''
            # header
    is_home = 'yes'
        # ====
    slider_data = Sliders.objects.all()
    
    cat = category.objects.all()
    products = product_master.objects.all()
    
    total = 0
    for data in cart_product:
        total += int(data.amount)
    return render(request, "index.html",{'is_home':'yes','sliders':slider_data,'category':cat,'cart_product':cart_product,'products':products,'cart_total':total,'user_id':user_id,'user':user})


def category_page(request,id):
    products = product_master.objects.filter(cat_id=id).all()
    cat = category.objects.all()
    if 'xyz' in request.session:
        user_id = request.session['xyz']        
    else:
        user_id = ''
    return render(request, "category.html",{'products':products,'category':cat,'user_id':user_id})

def subcategory_page(request,id):
    if 'xyz' in request.session:

        user_id = request.session['xyz']
        user = new_register.objects.filter(id=user_id).get()

    else:
        user_id = ''
        # if page is not login 
        user = ''
    products = product_master.objects.filter(sub_cat=id).all()
    sizes = size_master.objects.all()
    cat = category.objects.all()
    
    return render(request, "category.html",{'products':products,'category':cat,'user_id':user_id,'user':user,'sizes':sizes})

def brands_pg(request,id):
    if 'xyz' in request.session:
        user_id = request.session['xyz']
        user = new_register.objects.filter(id=user_id).get()
    else:
        user_id = ''
        user = ''
    products = product_master.objects.filter(brand_id=id).all()
    sizes = size_master.objects.all()
    cat = category.objects.all()
    
    return render(request, "brands.html",{'products':products,'category':cat,'user_id':user_id,'user':user,'sizes':sizes})


def product_page(request):
    if 'xyz' in request.session:
        user_id = request.session['xyz']
    else:
        user_id = ''
    cat = category.objects.all()
    products = product_master.objects.all()
    return render(request, "product.html",{'category':cat,'products':products,'user_id':user_id})

def cart_page(request):
    if 'xyz' in request.session:
        user_id = request.session['xyz']
    else:
        user_id = ''
    user = new_register.objects.filter(id=user_id).get()

    # ================its for cart page tamplate ===================
    sizes = size_master.objects.all()
    cart_product = add_to_cart.objects.filter(user_id=user_id).all()
    total = 0
    for data in cart_product:
        total += int(data.amount)
    # ==============================================
    return render(request, "cart.html",{'user_id':user_id,'user':user,'sizes':sizes,'cart_product':cart_product,'cart_total':total})

def checkout_page(request):
    msg = ""
    if 'xyz' in request.session:
        user_id = request.session['xyz']
    else:
        user_id = ''
    user = new_register.objects.filter(id=user_id).get()
    # ================its for cart in chackout page ===================
    sizes = size_master.objects.all()
    cart_product = add_to_cart.objects.filter(user_id=user_id).all()
    u = new_register.objects.filter(id = user_id).get()
    total = 0
    for data in cart_product:
        total += int(data.amount)
        # -------to show cart ids in checkout_register (selected products from user)
    if "checkout" in request.POST:

        cart_ids_list = []
        for row in cart_product:
            cart_ids_list.append(row.id)
        Email = request.POST['Email']
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Address = request.POST['Address']
        Country = request.POST['Country']
        State = request.POST['State']
        PostCode = request.POST['PostCode']
        Amount = request.POST['Amount']
        
        if Email == "":
            msg = "please enter Email"
        elif Firstname == "":
            msg = "please enter Firstname"
        elif Lastname == "":
            msg = "please enter Lastname"
        elif Address == "":
            msg = "please enter Address"
        elif Country == "":
            msg = "please enter Country"
        elif State == "":
            msg = "please enter State"
        elif PostCode == "":
            msg = "please enter PostCode"
        else:
            obj = chackout_register(
                Email = Email,
                Firstname = Firstname,
                Lastname = Lastname,
                Address = Address,
                Country = Country,
                State = State,
                PostCode = PostCode,
                user_id = u,
                cart_ids = cart_ids_list,
                Amount = Amount,
            )
            obj.save()
            checkout_info =chackout_register.objects.latest('id')
            request.session['checkout_id'] =checkout_info.id
            return redirect('/payment_demo/')
                            # -----------
    
    return render(request, "checkout.html",{'user_id':user_id,'user':user,'sizes':sizes,'cart_product':cart_product,'cart_total':total,'msg':msg})


def prod_master(request,id):
    if 'xyz' in request.session:
        user_id = request.session['xyz']
        user = new_register.objects.filter(id=user_id).get()
           
    else:
        return redirect('/login/')
        
        # 'add_cart' hase defined in botton of (aad to cart) in product page
    if 'add_cart' in request.POST:

        product_id = request.POST['pro_id']
        pro_id = product_master.objects.filter(id=product_id).get()
        user = new_register.objects.filter(id=user_id).get()
        qty = int(request.POST['qty'])
        pro_price = int(request.POST['pro_price'])
        p_amount = qty*pro_price
        cart_data = add_to_cart.objects.filter(product_id=pro_id,user_id=user_id)
        if cart_data.count() >= 1:
            row = cart_data.first()
            qty = int(row.qty) +1
            row.qty = qty
            p_amount = qty*pro_price
            row.amount = p_amount
            row.save()
        else:  
            obj = add_to_cart(
                product_id=pro_id,
                qty=qty,
                price=pro_price,
                amount=p_amount,
                user_id = user,
            )
            obj.save()
    
    
    cart_product = add_to_cart.objects.filter(user_id=user_id).all()
    total = 0
    for data in cart_product:
        total += int(data.amount)
    sizes = size_master.objects.all()
    cat = category.objects.all()
    products = product_master.objects.filter(id=id).first()
   
    return render(request, "product.html",{'products':products,'user_id':user_id,'category':cat,'sizes':sizes,'cart_product':cart_product,'cart_total':total,'user':user})


def remove_cart_prod(request,id):
    add_to_cart.objects.filter(id=id).delete()
    return redirect('home')

def login_page(request):
    
    msg = ''    
    if request.method=='POST':
        Emailaddress = request.POST['Emailaddress']
        Password = request.POST['Password']
        user_exist = new_register.objects.filter(Emailaddress=Emailaddress,Password=Password)
        if user_exist.count() == 1:
            user = user_exist.get()
            request.session['xyz'] = user.id
            return redirect('home')
        else:
            msg = "Invalid Email or password"
    return render(request, "login.html",{'msg':msg})

def register_page(request):
    msg = ""
    if 'Firstname' in request.POST:
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Emailaddress = request.POST['Emailaddress']
        Password = request.POST['Password']
        if Firstname == "":
            msg = "please enter firstname"
        elif Lastname == "":
            msg = "please enter lastname"
        elif Emailaddress == "":
            msg = "please enter Emailaddress"
        elif Password == "":
            msg = "please enter Password"
        else:
            obj = new_register(
                Firstname = Firstname,
                Lastname = Lastname,
                Emailaddress = Emailaddress,
                Password = Password,
            )
            obj.save()
    return render(request, "register.html",{"msg":msg})

def logout_req(request):
    del request.session['xyz']
    return redirect('/login')
    

def edit_profile(request):
    id = request.session['xyz']
    user = new_register.objects.filter(id=id).get()
    if 'Firstname' in request.POST:
        Firstname = request.POST['Firstname']
        Lastname = request.POST['Lastname']
        Emailaddress = request.POST['Emailaddress']
        # Password = request.POST['Password']

        user.Firstname = Firstname
        user.Lastname = Lastname
        user.Emailaddress = Emailaddress
        # user.Password = Password
        user.save()
    return render(request,'edit.html',{'user':user})

def change_password(request):
    msg = ''
    id = request.session['xyz']
    user = new_register.objects.filter(id=id).get()
    if request.method == 'POST':
        password = request.POST['password']
        newpassword = request.POST['newpassword']
        conformpassword = request.POST['conformpassword']
        if user.Password != password:
            msg = 'old password dose not match'
        elif newpassword != conformpassword:
            msg = 'password and conform password dose not match'
    
        else:
            msg = 'success'
            user.Password = newpassword
            user.save()
          
    return render (request,'change_password.html',{'msg':msg,'user':user})


# ---------------------------------ajax--------------------------------

def ajax_call(request):
    countries = Country.objects.all()
    return render(request,'ajax_demo.html',{'countries':countries})

def ajax_get_data(request):
    val = request.GET['searchVal']
    products = product_master.objects.filter(title__contains=val).all()
    return render(request,'ajax.html',{'products':products})

def ajax_get_states(request):
    val = request.GET['c_id']
    States = states.objects.filter(c_id=val).all()
    return render(request,'ajax_state.html',{'States':States})


# ----------------delete - brands - sub category - category - product -------------------

def cate_view(request):
    data = category.objects.all()
    return render(request,'cate_view.html',{'data':data})

def cate_delete(request,id):
    category.objects.filter(id=id).delete()
    return redirect('/cate_view/')

def subcate_view(request):
    data = sub_category.objects.all()
    return render(request,'subcate_view.html',{'data':data})

def subcate_delete(request,id):
    sub_category.objects.filter(id=id).delete()
    return redirect('/subcate_view/')

def view_brands(request):
    brands_data = brands.objects.all()
    return render(request,'brands_view.html',{'brands_data':brands_data})

def brands_delete(request,id):
    brands.objects.filter(id=id).delete()
    return redirect('/view_brands/')


def delete_pro(request,id):
    product_master.objects.filter(id=id).delete()
    return redirect('/view_product')

def view_product(request):
    view_data = product_master.objects.all()
    return render(request,'product_view.html',{'view_data':view_data})

# ---------------------razorpay--------------------`    `

def payment_demo(request):
    checkout_id =request.session['checkout_id']
    objdata=chackout_register.objects.filter(id=checkout_id).get()

    return render(request, "payment_index.html",{'data':objdata})

def order_payment(request):
    checkout_id =request.session['checkout_id']
    if request.method == "POST":
        
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create(
            {"amount": int(amount) * 100, "currency": "INR", "payment_capture": "1"}
        )
        order = Order.objects.create(
            name=name, amount=amount, provider_order_id=razorpay_order["id"]
        )
        order.save()
        return render(
            request,
            "payment.html",
            {
                "callback_url": "http://" + "127.0.0.1:8000" + "/callback/"+str(checkout_id),
                "razorpay_key": RAZORPAY_KEY_ID,
                "order": order,
                "checkout_id":checkout_id
            },
        )
    return render(request, "payment.html",{"checkout_id":checkout_id})


@csrf_exempt
def callback(request,id):
    print(id) 
    #checkout_id = request.POST.get('checkout_id','')
    def verify_signature(response_data):
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)
    
    # print("checkout id=",checkout_id)
    obj = chackout_register.objects.filter(id=id).get()
    obj.pay_status ="paid"    
    obj.save()
    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()

        if not verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})
