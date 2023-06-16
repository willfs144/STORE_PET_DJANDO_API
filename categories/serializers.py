from .models import Category

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import (
    SerializerMethodField
)

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'