from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializers


from rest_framework.generics import (CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView,
    ListAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView)

class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializers
    queryset =  Order.objects.all()
    
