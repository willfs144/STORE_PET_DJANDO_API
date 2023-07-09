
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate

from products.models import Product


def index(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Benvenido {} '.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
        
    return productList(request)

def productList(request):
    products = Product.objects.all().order_by('-id')
    
    return render(request, 'index.html', {
        #context
		 'message': "Listado de productos", 
		 'title': "Productos",
		 'products': products
         
    })

  
           
  


  