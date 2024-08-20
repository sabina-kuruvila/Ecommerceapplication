from django.shortcuts import render

from shop.models import Product

# Create your views here.

def base(request):
    return render(request,"shop/base.html")

def home(request):
    return render(request,"shop/home.html")

def product_list(request):
    products= Product.objects.all()
    return render(request,"shop/product_list.html",{"products": products})

def product_detail(request,id):
    product= Product.objects.get(pk=id)
    return render(request,"shop/product_detail.html",{"product": product})

def contact(request):
    return render(request,"shop/contact.html")

def about(request):
    return render(request,"shop/about.html")