from .models import Product

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    SerializerMethodField
)
from rest_framework import serializers

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


