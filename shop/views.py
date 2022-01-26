from django.shortcuts import render, get_object_or_404
from numpy import product
from .models import Product
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
    product = get_object_or_404(Product, id=id)
    return render(request, 'shop/details.html', {"product":product})