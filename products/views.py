from typing import Any, Dict

from products.models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin # solicita validaccion para acceder al api

from rest_framework.decorators import permission_classes
#Librerias para la API
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, RetrieveDestroyAPIView, RetrieveAPIView)

from .serializers import ProductSerializer

# Create your views here.
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')
    

    #pasa el contexto de la clase al template
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        context['products'] = context['product_list']
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'



#Listado API
#@permission_classes((AllowAny, ))
class ProductListAPI(ListAPIView):  
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer    

class ProductUpdateAPI(RetrieveUpdateAPIView):     
     #queryset = Product.objects.filter(price__gte=20000).order_by('-id') 
     queryset = Product.objects.all().order_by('-id')
     serializer_class = ProductSerializer 

class ProductCreateAPI(CreateAPIView):     
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPI(RetrieveAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPI(RetrieveDestroyAPIView):
    queryset =  Product.objects.all()
    serializer_class = ProductSerializer








