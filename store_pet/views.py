
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product
#from products import views
from django.contrib.auth import login
from django.contrib.auth import authenticate


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            print("Usuario autenticado")
        else:
            print("Usuario no autenticado")

  
           
    products = Product.objects.all().order_by('-id')
    
    return render(request, 'index.html', {
        #context
		 'message': "Listado de productos", 
		 'title': "Productos",
		 'products': products
         
    })


  