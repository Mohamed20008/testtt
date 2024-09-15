from django.shortcuts import render
from .models import Product

# Create your views here.
def product(request):
    return render(request, 'products/product.html',)
def products(request):
    pro = Product.objects.all().filter(name='oppo').order_by('name').exclude(category='phone')
    return render(request, 'products/products.html', {'pro': str(pro.count())} )
# def products(request):
#     return render(request, 'products/products.html', {'pro': str(Product.objects.all().filter(name='oppo').order_by('name').count())} )
# def products(request):
#     return render(request, 'products/products.html', {'pro': Product.objects.get(name='hello')} )
# def products(request):
#     return render(request, 'products/products.html', {'pro': Product.objects.all()} ) 
