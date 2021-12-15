from django.db.models.expressions import F
from django.forms import fields
from django.http import request
from django.shortcuts import redirect, render
from core.models import User,Userform
from products.models import add_product_class,Category,Product
# from .forms import add_product_form
from django.utils.text import slugify
from .models import Sales_records_total,Sales_records_individual
def dashboard(request):
    my_product_types = Category.objects.all()
    current_sales_records = Sales_records_total.objects.get(id=1)
    try:
        user_sales_records = Sales_records_individual.objects.get(user = request.user)
    except Sales_records_individual.DoesNotExist:
        user_sales_records = None
    if user_sales_records == None :
        none_image_for_sales = True
    else:
        none_image_for_sales = False
    context = {"product_types":my_product_types,"current_sales_records":current_sales_records,"user_sales_records":user_sales_records,"None_image":none_image_for_sales}
    return render(request,"home/dashboard.html",context)

def add_product(request,keyward):
    form  = add_product_class(request.POST,request.FILES)
    
    product_category = Category.objects.get(title = keyward)
    if request.method == 'POST':
       if form.is_valid():
            product_image_local = request.FILES.get('product_image')
            if product_image_local is None:
                product_image_local = 'Products/product.png'
            m = Product.objects.create(
            user = request.user,
            category = product_category,
            title = request.POST.get('title'),
            price = request.POST.get('price'),
            unit = request.POST.get('unit'),
            is_active = True,
            is_featured = False,
            short_description = request.POST.get('short_description'),
            sku = request.user.username + "-" + product_category.title[0:3] + "-" + request.POST.get('title') + "-" + request.POST.get('price'),
            slug = slugify(request.user.username + "-" + product_category.title[0:3] + "-" + request.POST.get('title') + "-" + request.POST.get('price')),
            
            product_image = product_image_local,
            

            )
           
            available_products_change = Category.objects.get(title = keyward)
            available_products_change.available_products = available_products_change.available_products + 1
            available_products_change.save()
            return redirect('dashboard')
       else:
            print("error occured")
    else: 
      print("erooe happen")
    context = {"add_products":form}
    # form  = add_product_form(request.POST)
    # product_category = Category.objects.get(title = keyward)
    # if request.method == 'POST':
    #     if form.is_valid():
    #         form.fields['product_category'] = product_category
    #         title = form.cleaned_data['product_title']
    #         price = form.cleaned_data['product_price']
    #         description = form.cleaned_data['description']
    #         sku = request.user.username + "-" + product_category.title[0:3] + "-" + form.fields('product_title') + "-" + form.fields('product_price')
    #         m = Product(category = product_category,title=title,price=price,is_active =True,is_featured=False,sku = sku,short_description = description )
    # context = {'add_products':form}
    return render(request,'home/add-product.html',context)

def products(request):
 products_in_market = Product.objects.all()[:3]
 context = {'products':products_in_market}
 return render(request,'home/products.html',context)

def profile(request,user_id):
    user_details = User.objects.get(id = user_id)
    context = {'user_form':user_details}
    return render(request,'home/settings.html',context)

def updateuser(request):

    user = request.user
    form = Userform(instance=user)
    if request.method == 'POST':
        form = Userform(request.POST,request.FILES,instance = user)
        print("method is POST")
        if form.is_valid():
            print("form is valid")
            form.save()
            print("form saved")
            return redirect('update_user')
    context = {'user_form':form}
    return render(request,'home/settings.html',context)
def contactdetails(request):
    user = request.user
    form = Userform(request.POST,request.FILES,instance = user)
    
    current_progress = Sales_records_total.objects.get(id =1 )
    current_progress.Total_users_involved = current_progress.Total_users_involved + 1
    current_progress.save()
    user_role = request.POST.get('user_role_in_market')
    print(user_role)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('dashboard')
    context = {'user_form':form}
    return render(request,'home/settings.html',context)