from django.shortcuts import render, get_object_or_404
from numpy import product
from .models import Product, Order
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    products = Product.objects.all()
    if request.method == 'POST':
        title = request.POST.get('prod_title')
        if title != '' and title is not None:
            products = products.filter(title__icontains = title)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'shop/index.html', {"products" : products})

def details(request, id):
    product_object = get_object_or_404(Product, id=id)
    return render(request, 'shop/details.html', {"product_object":product_object})

def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()

    return render(request,'shop/checkout.html')