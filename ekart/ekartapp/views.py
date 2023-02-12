from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Register, Products, Cart,Address
from django.contrib.auth import login as auth_login, authenticate, logout

# Create your views here.

# main page


def index(request):
    product_data = Products.objects.all()
    return render(request, 'index.html', {'data': product_data})


# login

def login(request):
    return render(request, 'login.html')


# admin page

def admin_page(request):
    return render(request, 'admin.html')


# mycart

def my_cart(request):
    cart_data = Cart.objects.filter(user=request.user)
    total=0
    for i in cart_data:
        total+=i.quantity*i.product.price

    all_data={'data':cart_data,'total':total}

    print('total',total)

    return render(request, 'mycart.html', all_data)


# registration

def register(request):
    return render(request, 'userregister.html')


# all products admin

def admin_all_products(request):

    product_data = Products.objects.all()
    return render(request, 'adminallproducts.html', {'products': product_data})


# registration

def user_register(request):
    if request.method == 'POST':
        user_name = request.POST['uname']
        fname = request.POST['firstname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = 'customer'

        if password == confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    email=email, first_name=fname, username=user_name, password=password)
                user.save()

                data = Register(user=user, role=role, first_name=fname, username=user_name, last_name=lname,
                                email=email, phone=phone, password=password, confirm_password=confirm_password)
                data.save()
                messages.info(
                    request, 'Registration successfull , please login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

        return render(request, 'login.html')
    else:
        return render(request, 'register')

#address input

def address(request):
    if request.method=='POST':
        address=request.POST['address']
        pincode=request.POST['pincode']
        city=request.POST['city']
        area=request.POST['area']
        district=request.POST['district']
        state=request.POST['state']

        data=Address(address=address,pincode=pincode,city=city,area=area,district=district,state=state)
        data.save()

        return redirect('profile')
    else:
        return redirect('profile')


        
# login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['luser']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        data = User.objects.filter(username=username).values()

        role = ''

        for i in data:
            u_username = i['username']

            user_data = Register.objects.filter(username=username).values()
            for i in user_data:
                role = i['role']

            if user is not None and username == u_username and role == 'customer':
                auth_login(request, user)
                return redirect('login_index')
            elif username == 'admin' and password == '12345':
                auth_login(request, user)
                return redirect('adminpage')
            else:
                pass

        else:
            messages.info(request, 'invalid credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


# logout

def user_logout(request):
    logout(request)
    messages.info(request, 'successfully logout')
    return redirect('index')


# page after login
def login_index(request):
    items = Cart.objects.filter(user=request.user)
    number = 0
    for i in items:
        number += 1

    product_data = Products.objects.all()
    content = {'data': product_data, 'number': number}
    return render(request, 'login_index.html', content)


# add product page in admin all products

def add_product_page(request):
    return render(request, 'addproduct.html')


# add product

def add_product(request):

    if request.method == 'POST':
        pname = request.POST['p_name']
        category = request.POST['p_category']
        price = request.POST['p_price']
        discription = request.POST['p_description']
        image = request.FILES['image']

        data = Products(product_name=pname, category=category,
                        price=price, description=discription, product_image=image)
        data.save()

        return redirect('adminallproducts')
    else:
        return redirect('adminallproducts')


# edit product handler

def edit_product_page(request, product_id):
    data = Products.objects.get(id=product_id)
    return render(request, 'admin_edit_product.html', {'data': data})


def edit_product_handler(request, product_id):
    data = Products.objects.get(id=product_id)
    data.product_name = request.POST['e_name']
    data.category = request.POST['e_category']
    data.price = request.POST['e_price']
    data.description = request.POST['e_discription']
    data.product_image = request.FILES['ed_image']
    data.save()

    data.save()
    return redirect('adminallproducts')


# delete products

def delete_product(request, product_id):
    data = Products.objects.get(id=product_id)
    data.delete()
    return redirect('adminallproducts')


# add to cart

def add_to_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(
        product=product, user=request.user, quantity=0)
    cart.quantity += 1
    cart.save()
    return redirect('mycart')


def remove_from_cart(request, product_id):
    product =Cart.objects.get(id=product_id)
    product.delete()
    return redirect('mycart')

# profile section

def profile(request):
    if request.user:
        user_data = Register.objects.filter(user=request.user)

        return render(request, 'profile.html', {'data': user_data})


# edit profile
def edit_profile(request, user_id):
    user_data = Register.objects.get(id=user_id)
    return render(request, 'edit_profile.html', {'data': user_data})


def edit_profile_handler(request, id):
    if request.method == 'POST':
        user_data = Register.objects.get(id=id)
        user_data.first_name = request.POST['first_name']
        user_data.last_name = request.POST['last_name']
        user_data.email = request.POST['edit_email']
        user_data.phone = request.POST['edit_phone']

        return redirect('profile')
