from rest_framework import serializers
from .models import Product, StockHistory


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class StockHistorySerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    updated_by = serializers.StringRelatedField()

    class Meta:
        model = StockHistory
        fields = '__all__'
