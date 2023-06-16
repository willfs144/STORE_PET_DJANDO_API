from typing import Any, Dict
from django.shortcuts import render

from products.models import Product

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
#Librerias para la API
from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)

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
class ProductListApi(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().order_by('-id')



