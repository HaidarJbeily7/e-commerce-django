from django.shortcuts import render
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