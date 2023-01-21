from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Register
from django.contrib.auth import login as auth_login,authenticate,logout

# Create your views here.

#main page

def index(request):
    return render(request,'index.html')


#login

def login(request):
    return render(request,'login.html')


#admin page

def admin_page(request):
    return render(request,'admin.html')


#mycart

def my_cart(request):
    return render(request,'mycart.html')


#registration

def register(request):
    return render(request,'userregister.html')

#all products admin

def admin_all_products(request):
    return render(request,'adminallproducts.html')



#registration

def user_register(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        fname=request.POST['firstname']
        lname=request.POST['lname']
        email=request.POST['email']
        phone=request.POST['mobile']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        role='customer'

        if password==confirm_password:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(email=email,first_name=fname,username=user_name,password=password)
                user.save()

                data=Register(user=user,role=role,first_name=fname,username=user_name,last_name=lname,email=email,phone=phone,password=password,confirm_password=confirm_password)
                data.save()
                messages.info(request,'Registration successfull , please login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')
        
        return render(request,'login.html')
    else:
        return render(request,'register')


#login 

def user_login(request):
    if request.method=='POST':
        username=request.POST['luser']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        data=User.objects.filter(username=username).values()
        
        role=''
        
        for i in data:
            u_username=i['username']

            user_data=Register.objects.filter(username=username).values()
            for i in user_data:
                role=i['role']

            if user is not None and username==u_username and role=='customer':
                auth_login(request,user)
                return redirect('login_index')
            elif username=='admin' and password=='12345':
                auth_login(request,user)
                return redirect('adminpage')
            else:
                pass


        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')



# logout 

def user_logout(request):
    logout(request)
    messages.info(request,'successfully logout')
    return redirect('index')

def login_index(request):
    return render(request,'login_index.html')



#add product page in admin all products

def add_product_page(request):
    return render(request,'addproduct.html')


#add product

def add_product(request):
    if request.method=='POST':
        pname=request.POST['p_name']
        category=request.POST['p_category']
        price=request.POST['p_price']
        discription=request.POST['p_description']
        image=request.FILES['p_image']



    return redirect('adminallproduct')



        



            

            
    
