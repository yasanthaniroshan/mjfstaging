from django.shortcuts import render
from .models import Category,Product 

# Create your views here.
def home(request):
    categories = Category.objects.filter(is_active = True)[:3]
    products = Product.objects.filter(is_active = True)[:10]
    context = {
        'categories' : categories,
        'products' : products,
    }
    return render(request,'store.html',context)