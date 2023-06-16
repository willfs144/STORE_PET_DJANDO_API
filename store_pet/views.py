
from django.shortcuts import render

from products.models import Product

def index(request):
    
    products = Product.objects.all().order_by('-id')
    
    return render(request, 'index.html', {
        #context
		 'message': "Listado de productos", 
		 'title': "Productos",
		 'products': products
    })