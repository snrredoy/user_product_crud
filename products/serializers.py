from rest_framework import serializers
from .models import Product
from customAbstractUser.serializers import UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'description', 'owner']
        # fields = '__all__'