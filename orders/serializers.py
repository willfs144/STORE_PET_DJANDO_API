from .models import Order
from rest_framework.serializers import ModelSerializer


class OrderSerializers(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'