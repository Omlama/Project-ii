from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password , check_password
from .models.customer import Customer
from .models.product import Product
from .models.category import Category
from django.http import HttpResponse


def home(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_product_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
        
    # pro = Product.get_all_products()
    data = {}
    # data['products'] = pro
    data['products'] = products
    data['categories'] = categories
    return render(request, 'Home.html', data)

def get_products(request,id):
    prods =Product.objects.filter(id = id).first()
    Product=prod.category.all().value_list('name',flat=True)
    context = {
        'prod':prods,
        'product': product
    }
    return render(request,'product_single.html', context)



def Aboutus(request):
    return render(request, 'Aboutus.html')

def Login(request):
    if request.method == 'GET':
        return render(request, 'Signin.html')
    else:
        email = request .POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag :
                return redirect('home')
            else:
                 error_message = 'Invalid email or password'
        else:
            error_message = 'Invalid email or password'
        print (email, password)
        return render(request, 'Signin.html')

def Signup(request):
    if request.method == 'GET':
        return render(request, 'Signups.html')
    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        
        customer = Customer (first_name=first_name, 
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             password=password)
        
        customer.password = make_password(customer.password)
        customer.signed()
        return redirect('home')
    
    
def Index(request):
    return render(request, 'index.html')

def get_products(request, id):
    p = Product.objects.get(id=id)
    # Product=prod.category.all().values_list('name',flat=True)
    # context = {
    #     'prod':prod,
    #     'product': product
    # }
    return render(request,'product_single.html', {'product':p})

def Search(request):
    return render(request,'search.html')