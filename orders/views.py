from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializers


from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)

# solicita validaccion para acceder al api
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin 

#Seccion de APIs
class OrderCreateAPIView(PermissionRequiredMixin, CreateAPIView):
    serializer_class = OrderSerializers
    queryset =  Order.objects.all()
    permission_required = 'store_pet.view_order'

#@permission_classes((AllowAny, ))
class OrderListApi(ListAPIView):
    serializer_class = OrderSerializers    
    queryset = Order.objects.all().order_by('-id')
    #queryset = Order.objects.filter(price__gte=20000).order_by('-id')
    
