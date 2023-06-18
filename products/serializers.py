from .models import Product

from rest_framework.serializers import ModelSerializer
from categories.serializers import CategorySerializer

class ProductSerializer(ModelSerializer):
    categoria = CategorySerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'


