from django.shortcuts import render,redirect

from administrator.models import Category, Product
from user.models import Cart, Register


# Create your views here.

def home(request):
    
    categories=Category.objects.all()
    products=Product.objects.all()
    uid=request.session.get('uid')
    if uid:
        user=Register.objects.get(id=uid)
        return render(request, 'index.html',{'uid':uid, 'user':user,'categories':categories,'products':products})
    else:
        return render(request, 'index.html',{'categories':categories,'products':products})
    


def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=Register.objects.get(email=email, password=password)
        if email == 'admin@gmail.com' and password == 'admin':
            request.session['rid']=user.id
            return redirect('admin_home')
        elif user:
            request.session['uid']=user.id
            return redirect('home')
        else:
            return render(request, 'login.html',{'error_msg':'Invalid credentials'})
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        count=Register.objects.filter(name=name,email=email, password=password).count()
        if count > 0:
            return render(request, 'register.html',{'error_msg':'Already registered user'})
        else:
            user=Register(name=name, email=email, password=password)
            res=user.save()
            return redirect('login')
    else:
        return render(request,'register.html')

def logout(request):
    if 'uid' in request.session:
        del request.session['uid']  
    return redirect('login')



def single_product(request,product):   
    uid=request.session.get('uid')
    if uid:
        user=Register.objects.get(id=uid)
    product=Product.objects.get(id=product)
    return render(request, 'SingleProduct.html',{'product':product,'uid':uid,'user':user})

def add_to_cart(request,product):
    uid=request.session.get('uid')
    if uid:
        pro=Product.objects.get(id=product)
        count=Cart.objects.filter(product_id=product,user_id=uid).count()
        if count >0:
            return render(request, 'SingleProduct.html',{'product':pro})
        else:
            data=Cart(product_id=product,user_id=uid,quantity=1)
            data.save()
            return render(request, 'SingleProduct.html',{'product':pro})
    else:
        return redirect('login')

def cart_view(request):
    uid=request.session.get('uid')
    if uid:
        user=Register.objects.get(id=uid)
        cart_items=Cart.objects.filter(user_id=uid)
        products = Product.objects.all() 
        return render(request, 'Cart.html', {'cart_items': cart_items, 'products': products, 'uid': uid, 'user': user})
       
    else:
        return redirect('login')
