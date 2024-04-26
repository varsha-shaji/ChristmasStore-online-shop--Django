from django.shortcuts import render,redirect
from user.models import Register
from administrator.models import Category,Product
from django.db.models import Q
# Create your views here.
def admin_home(request):
    rid=request.session.get('rid')
    if rid:
        admin=Register.objects.get(id=rid)
        return render(request, 'adminindex.html',{'rid':rid,'admin':admin})
    else:
        return redirect('login')

def admin_logout(request):
    if 'rid' in request.session:
        del request.session['rid']  
    return redirect('login')


def add_new_category(request):
    rid=request.session.get('rid')
    if rid:
        data=Category.objects.all()
        admin=Register.objects.get(id=rid)
        if request.method == 'POST'and request.FILES['file']:
            title=request.POST.get('title')
            image=request.FILES['file']
            count=Category.objects.filter(title=title,image=image).count()
            if count ==1:
                return render(request, 'NewCategory.html',{'error_msg':'Category already exists','admin':admin})
                return redirect('view_category')
            else:
                category=Category(title=title, image=image)
                category.save()
               
                return render(request, 'ViewCategory.html',{'rid':rid,'admin':admin,'datas':data})
        else:
            return render(request, 'NewCategory.html',{'admin':admin})
    else:
        return redirect('login')

    
   


def add_new_product(request):
    rid=request.session.get('rid')
    if rid:
        categories=Category.objects.all()
        admin=Register.objects.get(id=rid)
        datas=Product.objects.all()
        if request.method == 'POST'and request.FILES['file']:
            title=request.POST.get('title')
            description=request.POST.get('description')
            category=request.POST.get('category')
            cat=Category.objects.get(id=category)
            price=request.POST.get('price')
            stock=request.POST.get('stock')
            image=request.FILES['file']
            count=Product.objects.filter(title=title,image=image,price=price,stock=stock,description=description,category=cat).count()
            if count ==1:
                return render(request, 'NewProduct.html',{'error_msg':'Product already exists','admin':admin,'categories':categories})
                return redirect('view_product')
            else:
                product=Product(title=title, image=image, price=price,stock=stock,description=description,category=cat)
                product.save()
               
                return render(request, 'ViewProduct.html',{'rid':rid,'admin':admin,'datas':datas,'categories':categories})
        else:
            return render(request, 'NewProduct.html',{'rid':rid,'admin':admin,'categories':categories})
    else:
        return redirect('login')


def view_categories(request):
    
    rid=request.session.get('rid')
    if rid:
        admin=Register.objects.get(id=rid)
        data=Category.objects.all()
        return render(request, 'ViewCategory.html',{'rid':rid,'admin':admin,'datas':data})
    else:
        return redirect('login')


def view_products(request):
    categories=Category.objects.all()
    rid=request.session.get('rid')
    if rid:
        admin=Register.objects.get(id=rid)
        datas=Product.objects.all()
        return render(request, 'ViewProduct.html',{'rid':rid,'admin':admin,'datas':datas})
    else:
        return redirect('login')


def updatecategory(request, category):
    rid = request.session.get('rid')
    
    if rid:
        admin = Register.objects.get(id=rid)
        datas = Category.objects.all()
        data = Category.objects.get(id=category)
        
        if request.method == 'POST' :
            title = request.POST.get('title')
            image = request.FILES['file']
            
            data.title = title
            data.image = image
            data.save()
            return render(request, 'ViewCategory.html', {'rid': rid, 'admin': admin, 'datas': datas})
        else:
            return render(request, 'UpdateCategory.html', {'admin': admin, 'data': data})
    else:
        return redirect('login')

def deletecategory(request, category):     
    rid=request.session.get('rid')
    if rid:
        datas=Category.objects.all()
        data=Category.objects.get(id=category)
        admin=Register.objects.get(id=rid)
        data.delete()
        return render(request, 'ViewCategory.html',{'rid':rid,'admin':admin,'datas':datas})
        
    else:
        return redirect('login')


def updateproduct(request, product):
    rid = request.session.get('rid')
    
    if rid:
        admin = Register.objects.get(id=rid)
        datas = Product.objects.all()
        data = Product.objects.get(id=product)
        categories=Category.objects.all()
        if request.method == 'POST' :
            title=request.POST.get('title')
            description=request.POST.get('description')
            
            price=request.POST.get('price')
            stock=request.POST.get('stock')
            image=request.FILES['file']
            category=request.POST.get('category')
            
            cat=Category.objects.get(id=category)
            data.title = title
            data.description = description
            data.price = price
            data.stock = stock
            data.category=cat
            data.image = image
            data.save()
            return render(request, 'ViewProduct.html', {'rid': rid, 'admin': admin, 'datas': datas})
        else:
            return render(request, 'UpdateProduct.html', {'admin': admin, 'data': data,'categories':categories})
    else:
        return redirect('login')

def deleteproduct(request, product):   
    rid=request.session.get('rid')
    if rid:
        datas=Product.objects.all()
        data=Product.objects.get(id=product)
        admin=Register.objects.get(id=rid)
        data.delete()
        return render(request, 'ViewProduct.html',{'rid':rid,'admin':admin,'datas':datas})
        
    else:
        return redirect('login')



def users(request):
    datas=Register.objects.all()
    return render(request, 'Users.html',{'datas':datas})