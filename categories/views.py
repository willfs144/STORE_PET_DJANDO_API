from django.shortcuts import render
from categories.models import Category
from rest_framework.generics import (ListAPIView)

from .serializers import CategorySerializer


# Create your views here.
#API 

class CategoryListApi(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-id')